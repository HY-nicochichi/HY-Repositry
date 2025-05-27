FROM python:3.13.0-slim

ENV PYTHONUNBUFFERED=1

COPY . /
WORKDIR /flaskapi

RUN pip install -r /requirements.txt

CMD ["sh", "/cmd.sh"]
