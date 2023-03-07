up:
	docker-compose up --build --scale worker=5 -d

down:
	docker-compose down
benchmark:
# You must `pip install locust`
	locust -f locustfile.py
recompose: down up