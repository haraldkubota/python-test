init:
	pip install -r requirements.txt

test:
	python -m unittest discover tests
	#py.test tests
	python -m doctest -v app/*.py

app:
	python main.py
	
.PHONY: init test app
