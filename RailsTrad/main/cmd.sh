sleep 5

rm -f /railsapp/tmp/pids/server.pid

rake db:create
rake db:migrate

rails t

rails s -b "0.0.0.0" -p 3000
