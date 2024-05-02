SHELL := /bin/bash

postgres:
	docker run --name postgres -e POSTGRES_PASSWORD=postgres -d postgres

migrations:
	alembic upgrade head

test-api: postgres
	pytest

build-api:
	cd api && docker build -t api-image .

run-api:
	cd api && docker run -d --name running-api -p 80:80 api-image

build-run-api: postgres build-api run-api

run-api-local:
	cd api && python3 -m uvicorn main:app --reload