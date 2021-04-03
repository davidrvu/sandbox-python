# DAVIDRVU - 2021-04-02

# PARA EJECUCION EN LA NUBE:
		gcloud config set project txd-ppto-corp
		gcloud app deploy app.yaml
		Acceso APP: https://test-message-user-dot-txd-ppto-corp.uk.r.appspot.com

# PARA EJECUCION LOCAL SEGUN SISTEMA OPERATIVO:
		1. (En windows) SET FLASK_APP=main.py
		1. (En Linux)   export FLASK_APP=main.py
		2. python -m flask run
		3. Visitar http://127.0.0.1:5000


# Respuesta a pregunta:

https://stackoverflow.com/questions/66639915/problem-running-flask-app-on-google-cloud-app-engine


I had the same problem: I needed to create a progress bar while the function is running, using Flask deployed in Google App Engine (GAE). I needed to work with a lot of data and I wanted to keep the user informed about the current state of the process (reducing the uncertainty of our clients).

Inspired by this [Medium post: How to generate multiple progress bars in a Flask app](https://medium.com/@sureshd_731/how-to-generate-multiple-progress-bars-in-a-flask-app-8e77c013a81d) from @Suresh Devalapalli and his [GIT](https://github.com/sureshgaussian/flask_multiple_prog_bars), I followed the same steps, and it worked perfectly in local Flask, but when I deployed this to GAE, not allowed me to dynamically see the outputs, instead, all the messages where shown together when the program reaches the 100%.

Reading more about the restrictions of GAE, I found that (as [@DazWilkin](https://stackoverflow.com/users/609290/dazwilkin) said) App Engine waits until the response is complete before it is sent to the client. Moreover, GAE apparently can only manage one thread each time, so the requiered behavior would be impossible because you needeed at least another thread that keep asking about the state of the backend.

Then I found the answer of [@Justin Beckwith](https://stackoverflow.com/users/178236/justin-beckwith) in [other StackOverflow question](https://stackoverflow.com/questions/39188736/google-app-engine-for-long-running-but-low-cpu-tasks-or-long-polling) that inspired me to read more about **"App Engine Flexible environment"**. I learned more from the [official documentation](https://cloud.google.com/appengine/docs/the-appengine-environments), where you can see the comparison between the "Standard environment" and "Flexible environment". For operation and cost restrictions, please read the official documentation. The key feature that could solve this problem is Background threads: "Yes, with restrictions" for Standard environment and just "Yes" for Flexible environment. This lead me to try the @Suresh Devalapalli solution deployed in GAE Flexible Environment. **For my surprise, it WORKED!!** The same behaviour in local Flask and in GAE Flex.

So, [@matilde](https://stackoverflow.com/users/15379244/matilde), I will show my codes that could help you:

# main.py

	# DAVIDRVU - 2021-04-02
	from flask import Flask, render_template, request, session, Response
	import time

	app = Flask(__name__)
	app.secret_key = "123"

	@app.route('/my_function')
	def my_function():
		arg1 = session.get('arg1')
		arg2 = session.get('arg2')
		arg3 = session.get('arg3')

		def generate(arg1, arg2, arg3):
			#Does something and defines string1
			time.sleep(2)
			string1 = "arg1 = " + str(arg1)
			yield "data:" + str(string1) + "\n\n"
		
			#Does something else and defines string2
			time.sleep(2)
			string2 = "arg2 = " + str(arg2)
			yield "data:" + str(string2) + "\n\n"
		
			#Does something else and defines string3
			time.sleep(2)
			string3 = "arg3 = " + str(arg3)
			yield "data:" + str(string3) + "\n\n"

			yield "data:END_SIGNAL\n\n"

		resp = Response(generate(arg1, arg2, arg3), mimetype= 'text/event-stream', headers={'X-Accel-Buffering': 'no'})
		return resp

	@app.route('/flask_post', methods=['POST'])
	def flask_post():
		session['arg1'] = request.form.get('arg1')
		session['arg2'] = request.form.get('arg2')
		session['arg3'] = request.form.get('arg3')
		return render_template('result.html')

	@app.route('/')
	def root():
		return render_template('index.html')

	if __name__ == "__main__":
		app.run(host='127.0.0.1', port=8080, debug=True)



Highlights from main.py:
1) The use of session to pass variables from one Flask function to another.
2) Explicit indicate the event-stream typ using: mimetype= 'text/event-stream'
3) Explicit indicate that you don't want buffering the outputs using: headers={'X-Accel-Buffering': 'no'}. If you don't configure the headers, you don't get the messages until the function ends.

# index.html

	<!DOCTYPE html>
	<html>
	<head>
	</head>

	<body>
		<form action="{{ url_for('flask_post') }}" method="POST">
		<input type="text" name="arg1">
		<input type="text" name="arg2">
		<input type="text" name="arg3">
		<input type="submit">
		</form>
	</body>
	</html>


# result.html

	<!DOCTYPE html>
	<html>
	<head>
		<script>
			var source = new EventSource("/my_function");
			document.open();
			source.onmessage = function(event) {
				if(event.data == "END_SIGNAL"){
					source.close()
				}
				else{
					console.log(event.data);
					document.write("<p>" + event.data +"</p>");
				}
			}
			document.close();
		</script>
	</head>
	<body>
	</body>
	</html>


Highlights from result.html:
The JavaScript calls "my_function" without parameters, and capture every message until the data come with the "END_SIGNAL". The parameters were obteined using session.get, which is a Flask work around.

# requirements.txt


    Flask
    gunicorn


# app.yaml


	#################################################################################
	# CASE 1: Standard environment AppEngine
	#################################################################################
	#runtime: python37

	#entrypoint: gunicorn -b :$PORT main:app

	#################################################################################
	# CASE 2: Flexible Environment AppEngine
	#################################################################################
	runtime: python
	env: flex
	runtime_config:
		python_version: 3

	manual_scaling:
	instances: 2
	resources:
	cpu: 1
	memory_gb: 4
	disk_size_gb: 10  # Disk size must be between 10GB and 10240GB

	entrypoint: gunicorn -b :$PORT main:app
	#################################################################################


Highlights from app.yaml:
**This is the most important part of this implementation**. I personally tested both Environmets and observe the different behaviours:

1) CASE 1 (commented lines), for the Standard environment deployment: When the function ends, the outputs appears.

2) CASE 2, for the Flexible Environment deployment: I finally obtained the desired behaviour, showing the messages from the backend to HTML in "real time" while the function is still working, allowing you to show the current state from the backend. Note the parameters required for each Environment are differents and the "deploy time" is longer in the Flex environment.

I hope this could help you!
