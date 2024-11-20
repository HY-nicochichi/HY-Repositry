FROM python:3.13.0-slim-bookworm

ENV PYTHONUNBUFFERED=1

COPY . /
WORKDIR /flaskapi

RUN pip install -r /requirements.txt

CMD sleep 5 && \ 
exec gunicorn --bind :5000 --workers 1 --threads 8 --timeout 0 core:app
