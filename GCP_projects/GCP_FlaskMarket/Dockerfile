FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED 1

COPY . /
WORKDIR /flaskapp

RUN pip install -r /requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app
