default:
	@cat makefile

reqs:
	. env/bin/activate; pip install -r requirements.txt

run:
	. env/bin/activate; python test.py

test:
	. env/bin/activate; pytest -vvx test.py
