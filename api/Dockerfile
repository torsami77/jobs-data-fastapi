FROM python:3.9

WORKDIR /code

ARG SQLALCHEMY_DATABASE_URL='postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'

ENV SQLALCHEMY_DATABASE_URL=$SQLALCHEMY_DATABASE_URL

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]