import time
import random
import math
import sympy as smp
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

N = 1034776851837418228051242693253376923
x = int(math.log10(N))+1

if (x < 25)
factor_base_size = 100
else
factor_base_size = (int)(2.93 * (x * x) - 164.4 * x + 2455)

x = 386 * (x * x) - 23209.3 * x + 352768


def get_new_d(D):
    '''
    Find the next prime after D that is a quadratic residue modulo N such that D = 3 (mod 4) */
    '''
    if D == 0:
        D = math.sqrt(N * 2)/2
        return D
    D = smp.nextprime(D)
    while ((smp.ntheory.legendre_symbol != 1) or (D % 4 != 3)):
        D = smp.nextprime(D)
    return D


def generate_new_polynomial(A, B, C, D):
    D = get_new_d(D)
    A = D*D
    h0 = N**((D-3) / 4)
    h1 = N**((D+1) / 4)
    h2 = (2*h1)**(-1)
    tmp = (N - h1**2)
    h2 = (2*h1)**(-1) * ((N - h1**2) / D)
    B = (h1 + h2*D) % A
    C = B*B
    C = N-C
    C = C // A
    C = -C 
    
    return (A, B, C, D)


"""
for i in range(numTasks):
    time.sleep(0.5)  # delay
    
    t = app.send_task('add', (i, 3))  # Send task by name
    tasks.append(t)
    print('Sent task:', i, t)

print('Finished sending tasks')
print(len(tasks))

for task in tasks:
    result = task.get()
    print('Received result:', result)

print('Applicati""
"""
