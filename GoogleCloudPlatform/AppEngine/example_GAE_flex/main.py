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