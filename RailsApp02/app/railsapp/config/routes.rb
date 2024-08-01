Rails.application.routes.draw() do
    root("root#index")
    get("/login", to: "sessions#new")
    post("/login", to: "sessions#create")
    delete("/logout", to: "sessions#destroy")
    resources(:users)  
end
