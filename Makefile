start:
	FLASK_APP=todolist flask run --reload

deps:
	pip install -r todolist/requirements.txt


create-venv:
	python3 -m venv ~/v3

test:
	python3 todolist/selenium_test.py --verbose
