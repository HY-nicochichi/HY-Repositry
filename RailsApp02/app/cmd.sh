# DBコンテナの起動が完了するまで5秒待つ(DB接続エラー防止策)
sleep 5

# pidファイルを消去して再起動可能に
rm -f /railsapp/tmp/pids/server.pid

rake db:create
rake db:migrate

rails s -b "0.0.0.0" -p 3000
