cd /railsapp

rake db:create
rake db:migrate

rails s -b '0.0.0.0' -p 3000
