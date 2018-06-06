from celery import Celery

app = Celery('our-dispatcher', broker='redis://localhost:6379/0')

app.conf.update(
    task_routes={'com.redhat.some.task': {'queue': 'com.redhat.some.task'}}
)

@app.task(name='com.redhat.some.task')
def some_task(x, y, message):
    print('{msg}: {z}'.format(msg=message, z=x+y))
