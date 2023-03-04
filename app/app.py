import time
import random

from celery import Celery

# Wait for rabbitmq to be started
time.sleep(20)

print('Application started')

app = Celery(
    'tasks',
    broker='pyamqp://user:bitnami@rabbitmq',
    backend='redis://redis',
)

numTasks = 10
tasks = []

for i in range(numTasks):
    time.sleep(0.5)  #  delay
    
    t = app.send_task('add', (i, 3))  # Send task by name

    print('Sent task:', i)
    print(t)
    print(t.status)
    print(t.state)
    print('Result', t.get())
print('Finished tasks')
print(len(tasks))

for task in tasks:
    result = task.get()
    print('Received result:', result)

print('Application ended')