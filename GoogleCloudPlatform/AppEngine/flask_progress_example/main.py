# 2021-03-13
# DAVIDRVU
# Fuente 1: https://github.com/djdmorrison/flask-progress-example/blob/master/app.py
# Fuente 2: ¿Cómo funciona? https://stackoverflow.com/questions/12232304/how-to-implement-server-push-in-flask-framework

from flask import Flask, render_template, Response, request, session
import platform
import time

app = Flask(__name__)

@app.route('/')
def root():
    system_name = platform.platform()
    return render_template('index.html',
                           system_name = system_name)

@app.route('/data_processing', methods=['POST'])
def data_processing():
    print("Starting data_processing")
    system_name = platform.platform()
    input_linea_sublinea = request.form["input_linea_sublinea"]
    input_marca          = request.form["input_marca"]

    print(request.form.get('input_opt1'))
    print(request.form.get('input_opt2'))
    print(request.form.get('input_opt3'))
    print(request.form.get('input_opt4'))

    if request.form.get('input_opt1') != None:
        input_opt1 = True
    else:
        input_opt1 = False

    if request.form.get('input_opt2') != None:
        input_opt2 = True
    else:
        input_opt2 = False

    if request.form.get('input_opt3') != None:
        input_opt3 = True
    else:
        input_opt3 = False

    if request.form.get('input_opt4') != None:
        input_opt4 = True
    else:
        input_opt4 = False

    print("input_linea_sublinea = " + str(input_linea_sublinea))
    print("input_marca          = " + str(input_marca))
    print("input_opt1           = " + str(input_opt1))
    print("input_opt2           = " + str(input_opt2))
    print("input_opt3           = " + str(input_opt3))
    print("input_opt4           = " + str(input_opt4))

    return render_template('test_progress_bar.html',
                           system_name = system_name,
                           input_linea_sublinea=input_linea_sublinea,
                           input_marca = input_marca,
                           input_opt1  = input_opt1,
                           input_opt2  = input_opt2,
                           input_opt3  = input_opt3,
                           input_opt4  = input_opt4 
                           )


@app.route('/progress')
def progress():
    def generate():
        x = 0
        
        #while x <= 100:
        #    yield "data:" + str(x) + "\n\n"
        #    x = x + 20
        #    time.sleep(0.5)

        dict_comm = '{"percent": "0", "message": "Procesando etapa 1 ..."}'
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(0.5)
        
        dict_comm = '{"percent": "10", "message": "Procesando etapa 2 ..."}'
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(0.5)

        dict_comm = '{"percent": "20", "message": "Procesando etapa 3 ..."}'        
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(0.5)

        dict_comm = '{"percent": "30", "message": "Procesando etapa 4 ..."}'        
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(0.5)

        dict_comm = '{"percent": "40", "message": "Procesando etapa 5 ..."}'        
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(1)

        dict_comm = '{"percent": "50", "message": "Procesando etapa 6 ..."}'        
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(1)

        dict_comm = '{"percent": "60", "message": "Procesando etapa 7 ..."}'        
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(3)

        dict_comm = '{"percent": "90", "message": "Procesando etapa 8 ..."}'                
        yield "data:" + str(dict_comm) + "\n\n"
        time.sleep(1)

        dict_comm = '{"percent": "100", "message": "Proceso finalizado exitosamente"}'                
        yield "data:" + str(dict_comm) + "\n\n"

    resp = Response(generate(), mimetype= 'text/event-stream', headers={'X-Accel-Buffering': 'no'})
    resp.headers["X-Accel-Buffering"] = "no"
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)