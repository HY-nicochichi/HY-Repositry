# DBコンテナの起動が完了するまで５秒待つ(DB接続エラー防止策)
sleep 5
exec gunicorn --certfile /crt.pem --keyfile /key.pem --bind 0.0.0.0:443 --workers 1 --threads 8 --timeout 0 run:app
