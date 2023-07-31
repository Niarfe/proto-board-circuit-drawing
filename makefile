default:
	@cat makefile

reqs:
	. env/bin/activate; pip install -r requirements.txt

run:
	. env/bin/activate; python draw_pcb.py test.pcb

test:
	. env/bin/activate; pytest -vvx draw_pcb.py
