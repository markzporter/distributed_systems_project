import time
from locust import HttpUser, task, between


class FactoringUser(HttpUser):

    @task
    def hello_world(self):
        print('First we do 60 bit')
        ints = [
            855852082054142051,
            792665042234851453,
            821540805765780943,
            664398872657467523,
        ]
        for i in ints:
            self.client.get(f'/api/factorize/{i}')
        print('Next we do 80 bit')
        ints = [
            959645548660089755728171,
            808267623222262673580091,
            977445261467952413278379,
            1082745516515618627335003,
        ]
        for i in ints:
            self.client.get(f'/api/factorize/{i}')
        print('Next do just one 120 bit')
        ints = [
            1039137903158703521332650183360460783
        ]
        for i in ints:
            self.client.get(f'/api/factorize/{i}')
