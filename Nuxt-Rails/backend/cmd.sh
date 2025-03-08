sleep 5

rm -f /railsapi/tmp/pids/server.pid

rake db:create
rake db:migrate

rails s -b "0.0.0.0" -p 5000
