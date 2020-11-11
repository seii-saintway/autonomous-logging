install:
	sudo -HE pip install -r requirements.txt

run:
	gunicorn -w 4 -b 0.0.0.0:8888 --log-config gunicorn-log.conf myapp:app 1> stdout.txt 2> stderr.txt
