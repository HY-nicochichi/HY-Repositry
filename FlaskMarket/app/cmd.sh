# DBコンテナのセットアップが完了するまで10秒待つ(DB接続エラー防止策)
sleep 10

# マイグレーション
flask db init
flask db migrate
flask db upgrade

# サーバー起動
exec gunicorn --certfile /crt.pem --keyfile /key.pem --bind 0.0.0.0:443 --workers 1 --threads 8 --timeout 0 run:app
