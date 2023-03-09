up:
	docker-compose up --build --scale worker=3

down:
	docker-compose down
benchmark:
# You must `pip install locust`
	locust -f locustfile.py
recompose: down up