FROM python:3.9

WORKDIR /code

ARG SECRET_KEY: 09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ARG ALGORITHM: HS256
ARG POSTGRES_USER="postgres"
ARG POSTGRES_PASSWORD="postgres"
ARG POSTGRES_SERVER="localhost"
ARG POSTGRES_DB="postgres"

ENV SECRET_KEY: 09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ENV ALGORITHM: HS256
ENV POSTGRES_USER: "postgres"
ENV POSTGRES_PASSWORD: "postgres"
ENV POSTGRES_SERVER: "localhost:5432"
ENV POSTGRES_DB: "postgres"

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]