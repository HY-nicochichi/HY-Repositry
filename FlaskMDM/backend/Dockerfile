FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED 1

COPY . /
WORKDIR /flaskapi

RUN pip install -r /requirements.txt

RUN mkdir /manager_keys

CMD sleep 5 && \ 
exec gunicorn --bind 0.0.0.0:5000 --workers 1 --threads 8 --timeout 0 run:app
