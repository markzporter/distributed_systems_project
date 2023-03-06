import time
import random
from quadratic_sieve import QS
import math
from flask import Flask, request, jsonify

from celery import Celery

# Wait for rabbitmq to be started
time.sleep(20)



print('Application started')

celery_app = Celery(
    'tasks',
    broker='pyamqp://user:bitnami@rabbitmq',
    backend='redis://redis',
)
api = Flask(__name__)


@api.route("/api/factorize/<N>", methods=['GET'])
def factorize(N):
    N = int(N)
    L = (math.e)**math.sqrt((math.log(N)*math.log(math.log(N))))
    B = int(L**(1/math.sqrt(2)))
    factors = QS(N, B, 10000000, celery_app)
    print('Got factors!')
    print(factors)
    return jsonify({'data': list(factors),  'status': 200}), 200

@api.route('/test', methods=['GET'])
def test():
    return jsonify('hello world')

@api.errorhandler(404)
def not_found(error):
    return jsonify({"msg": "Not Found", "status": 404}), 404

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=5000)