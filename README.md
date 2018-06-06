* Install redis-server and `pip install --user -r requirements.txt`
* Run redis-server
* Run `celery -A worker1 worker -Q com.redhat.some.task`
* Run `python server.py`
