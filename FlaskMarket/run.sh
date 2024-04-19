docker pull python:3.12-slim-bookworm
docker pull postgres:16-alpine

openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:2048 -out ./app/key.pem
openssl req -new -key ./app/key.pem -out ./app/csr.pem -subj "/C=JP/ST=Kyoto/L=Kyoto-shi/O=HY/CN=localhost"
openssl x509 -req -in ./app/csr.pem -signkey ./app/key.pem -days 365 -out ./app/crt.pem

docker compose up -d
