
install:
	pip install -r requirements.txt

test:
	pytest test/

lint:
	flake8 .

run:
	python main.py
