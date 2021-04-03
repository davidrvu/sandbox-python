# PARA EJECUCION EN LA NUBE:
		gcloud config set project txd-ppto-corp
		gcloud app deploy app.yaml
		Acceso APP: https://test-progress-bar-dot-txd-ppto-corp.uk.r.appspot.com

# PARA EJECUCION LOCAL SEGUN SISTEMA OPERATIVO:
		1. (En windows) SET FLASK_APP=main.py
		1. (En Linux)   export FLASK_APP=main.py
		2. python -m flask run
		3. Visitar http://127.0.0.1:5000