class SessionsController < ApplicationController

    # GET "/login"
    def new()
        if session["user"]
            return redirect_to("/", flash: {"danger"=>"※ 既にログイン済です"})
        else
            @user_info = {"login"=>false}
        end
    end

    # POST "/login"
    def create()
        if session["user"]
            return redirect_to("/", flash: {"danger"=>"※ 既にログイン済です"})
        else
            email = params["email"]
            pass = params["pass"]
            result = auth(email, pass)
            if result["message"] == "successed"
                log_in(result["user_id"])
                return redirect_to("/")
            else
                return redirect_to("/login", flash: {"danger"=>result["message"]})
            end
        end
    end

    # DELETE "/logout"
    def destroy()
        if session["user"]
            log_out()
            return redirect_to("/")
        else
            return redirect_to("/login")
        end
    end

end
