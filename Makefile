up:
	docker-compose up --build --scale worker=3

down:
	docker-compose down

recompose: down up