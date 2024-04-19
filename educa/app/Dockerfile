FROM python:3.12-slim-bookworm

RUN apt-get -y update && apt-get -y install gcc

WORKDIR /flaskapp
COPY . .

RUN pip install --no-cache-dir -r /flaskapp/config/requirements.txt
