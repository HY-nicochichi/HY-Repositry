Rails.application.routes.draw do

  post   "/jwt/"  => "jwt#post"

  get    "/user/" => "user#get"
  post   "/user/" => "user#post"
  put    "/user/" => "user#put"
  delete "/user/" => "user#delete"

end
