class RootController < ApplicationController

    # GET "/"
    def index()
        if session["user"]
            user = search_by_id(session["user"])
            @user_info = {"login"=>true, "id"=>user.id, "name"=>user.name}
        else
            @user_info = {"login"=>false}
        end
    end

end
