class UsersController < ApplicationController

    # GET "/users/1"
    def show()
        if session["user"]
            user = search_by_id(session["user"])
            @user_info = {"login"=>true, "id"=>user.id, "name"=>user.name, "email"=>user.email}
        else
            return redirect_to("/login")
        end
    end

    # GET "/users/new"
    def new()
        if session["user"]
            return redirect_to("/", flash: {"danger"=>"※ 既にログイン済です"})
        else
            @user_info = {"login"=>false}
        end
    end

    # GET "/users/1/edit"
    def edit()
        if session["user"]
            user = search_by_id(session["user"])
            @param = params["param"]
            @user_info = {"login"=>true, "id"=>user.id, "name"=>user.name}
        else
            return redirect_to("/login")
        end
    end

    # POST "/users"
    def create()
        if session["user"]
            return redirect_to("/", flash: {"danger"=>"※ 既にログイン済です"})
        else
            email = params["email"]
            pass = params["pass"]
            name = params["name"]
            result = register(email, pass, name)
        end
        if result["message"] == "successed"
            log_in(result["user_id"])
            return redirect_to("/")
        else
            return redirect_to("/users/new", flash: {"danger"=>result["message"]})
        end
    end

    # PATCH "/users/1"
    def update()
        if session["user"]
            param = params["param"]
            current_value = params["現#{param}"]
            new_value = params["新#{param}"]
            check_value = params["新#{param}(確認)"]
            if param == "メールアドレス"
                result = update_email(session["user"], current_value, new_value, check_value)
            elsif param == "パスワード"
                result = update_pass(session["user"], current_value, new_value, check_value)
            elsif param == "ユーザーネーム"
                result = update_name(session["user"], current_value, new_value, check_value)
            end
            if result == "success"
                return redirect_to("/users/#{session["user"]}")
            else
                return redirect_to("/users/#{session["user"]}/edit?param=#{param}", flash: {"danger"=>result}, allow_other_host: true)
            end
        else
            return redirect_to("/login")
        end
    end

    # DELETE "/users/1"
    def destroy()
        if session["user"]
            delete(session["user"])
            log_out()
            return redirect_to("/")
        else
            return redirect_to("/login")
        end
    end

end
