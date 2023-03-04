from celery import Celery

app = Celery('tasks', broker='pyamqp://user:bitnami@rabbitmq//',
             backend='redis://redis')


@app.task(name='add')
def add(x, y):
    return x + y
