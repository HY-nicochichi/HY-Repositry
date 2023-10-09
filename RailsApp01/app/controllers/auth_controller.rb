class AuthController < ActionController::Base

    # ログイン
    def login
        if session[:user]
            redirect_to("/")
        end
    end

    def login_post
        if session[:user]
            redirect_to("/")
        else
            require "digest"
            email = params[:email]
            pass = Digest::SHA256.hexdigest(params[:pass])
            if User.find_by(email: email) && User.find_by(email: email).pass == pass
                session[:user] = email
                redirect_to("/")
            else
                redirect_to("/login")
            end
        end
    end

    # ログアウト
    def logout
        if session[:user]
            session.clear
            redirect_to("/")
        else
            redirect_to("/login")
        end
    end

    # アカウント登録
    def signin
        if session[:user]
            redirect_to("/")
        end
    end

    def signin_post
        if session[:user]
            redirect_to("/")
        else
            require "digest"
            email = params[:email]
            pass = Digest::SHA256.hexdigest(params[:pass])
            name = params[:name]
            if User.find_by(email: email)
                redirect_to("/signin")
            else
                User.create(email: email, pass: pass, name: name)
                session[:user] = email
                redirect_to("/")
            end
        end
    end

    # アカウント削除
    def signout
        if session[:user]
            User.find_by(email: session[:user]).destroy
            session.clear
            redirect_to("/")
        else
            redirect_to("/login")
        end
    end

end
