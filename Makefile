env:
	virtualenv env

init:
	pip install -r requirements.txt

test:
	nosetests tests

serve:
	FLASK_APP=src/views.py FLASK_ENV=development flask run
