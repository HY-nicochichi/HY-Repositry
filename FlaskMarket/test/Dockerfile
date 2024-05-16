FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED 1

COPY . /
WORKDIR /testapp

RUN pip install -r /requirements.txt

CMD ["sh", "/cmd.sh"]
