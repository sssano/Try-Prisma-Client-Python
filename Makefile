build:
	docker-compose build app

up:
	docker-compose up -d

sample:
	docker-compose run --rm app python sample.py

down:
	docker-compose down

db_push:
	docker-compose run --rm app prisma db push

migrate:
	docker-compose run --rm app prisma migrate dev
