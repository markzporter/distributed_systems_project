import time
import random
from quadratic_sieve import QS
import math
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
N = 973225708688524723
L = (math.e)**math.sqrt((math.log(N)*math.log(math.log(N))))
B = int(L**(1/math.sqrt(2)))

print(QS(N, B, 100000, app))
