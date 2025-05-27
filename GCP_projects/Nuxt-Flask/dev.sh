docker pull node:23.11.0-slim
docker pull python:3.13.0-slim
docker pull nginx:1.27.5-alpine

docker run -t -d --name dev_nuxt-flask-frontend node:23.11.0-slim
docker run -t -d --name dev_nuxt-flask-backend python:3.13.0-slim
