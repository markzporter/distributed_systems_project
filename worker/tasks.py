from celery import Celery

app = Celery('tasks', broker='pyamqp://user:bitnami@rabbitmq//',
             backend='redis://redis')


# PLEASE NOTE:  Much of the code in this file has been adapted from 
# https://github.com/NachiketUN/Quadratic-Sieve-Algorithm
# See the license below. Much appreciation to Nachiket!! 


"""
MIT License

Copyright (c) 2023 Nachiket Umesh Naganure

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
@app.task(name='add')
def add(x, y):
    return x + y


@app.task(name='quad_residue_task')
def quad_residue_task(a, n):
    return quad_residue(a, n)


def quad_residue(a, n):
    # checks if a is quad residue of n
    l = 1
    q = (n-1)//2
    x = q**l
    if x == 0:
        return 1

    a = a % n
    z = 1
    while x != 0:
        if x % 2 == 0:
            a = (a ** 2) % n
            x //= 2
        else:
            x -= 1
            z = (z*a) % n

    return z

@app.task(name='STonelli')
def STonelli(n, p):  # tonelli-shanks to solve modular square root, x^2 = N (mod p)
    assert quad_residue(n, p) == 1, f"{n, p} not a square (mod p)"
    q = p - 1
    s = 0

    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        r = pow(n, (p + 1) // 4, p)
        return r, p-r
    for z in range(2, p):
        #print(quad_residue(z, p))
        if p - 1 == quad_residue(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return (r, p-r)
