docker pull python:3.12-slim-bookworm
docker pull nginx:1.25-alpine

openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:2048 -out key.pem
openssl req -new -key key.pem -out csr.pem -subj "/C=JP/ST=Kyoto/L=Kyoto-shi/O=HY/CN=localhost"
openssl x509 -req -in csr.pem -signkey key.pem -days 365 -out crt.pem

docker compose up -d
