Rails.application.routes.draw do

  root(to: "root#index")

  get("/session/new", to: "session#new")
  post("/session/create", to: "session#create")
  delete("/session/destroy", to: "session#destroy")

  get("/user/show", to: "user#show")
  get("/user/new", to: "user#new")
  get("/user/edit", to: "user#edit")
  post("/user/create", to: "user#create")
  put("/user/update", to: "user#update")
  delete("/user/destroy", to: "user#destroy")

end
