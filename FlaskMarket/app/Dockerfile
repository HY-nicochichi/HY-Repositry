FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED 1

COPY . /
WORKDIR /flaskapp

RUN pip install -r /requirements.txt

CMD ["sh", "/cmd.sh"]
