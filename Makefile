SHELL := /bin/bash

postgres:
	docker run --name postgres -e POSTGRES_PASSWORD=postgres -d postgres

migrations-up: 
	python3 -m alembic upgrade head

migrations-down:
	python3 -m alembic downgrade head-1

test-api: postgres 
	cd api && pip3 install --no-cache-dir --upgrade -r requirements.txt
	cd api && python3 -m alembic upgrade head
	cd api && python3 -m pytest --cache-clear    
	cd api && python3 -m alembic downgrade head-1

build-api-image:
	cd api && docker build -t api-image .

run-api-container:
	cd api && pip3 install --no-cache-dir --upgrade -r requirements.txt
	cd api && docker run -d --name running-api -p 80:80 api-image

build-run-api: postgres build-api-image run-api-container

run-api-local:
	cd api && python3 -m uvicorn main:app --reload

build-ui:
	cd ui && docker image build -t ui-image .

run-ui:
	cd ui && docker run -p 3000:3000 --name running-ui -p 80:80 ui-image
	
build-run-ui: build-ui run-ui

down:
	docker stop postgres
	docker stop running-ui
	docker stop running-api
	docker system prune -a -f