from celery import Celery

app = Celery('our-dispatcher', broker='redis://localhost:6379/0')

app.conf.update(
    task_routes={
        'com.redhat.some.task': {'queue': 'com.redhat.some.task'},
        'com.redhat.some.other.task': {'queue': 'com.redhat.some.other.task'}
    }
)

x = app.send_task('com.redhat.some.task', args=(1, 2), kwargs={'message': 'tadaaa'})
