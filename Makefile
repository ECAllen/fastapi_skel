snapshot:
	pip3 freeze > requirements.txt

install: 
	pip3 install --upgrade pip && pip3 install -r requirements.txt

lint:
	pylint --disable=R,C app/main.py

format:
	black app/main.py
	black app/*/*.py

test:
	python -m pytest -vv --cov=main test_main.py


