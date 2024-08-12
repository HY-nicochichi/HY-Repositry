Rails.application.routes.draw do

  post "/api/jwt/create"  => "jwt#create"

  post "/api/user/create" => "user#create"
  get  "/api/user/info"   => "user#info"
  post "/api/user/update" => "user#update"
  get  "/api/user/delete" => "user#delete"

end
