require "digest"

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
            email = params[:email]
            pass = Digest::SHA256.hexdigest(params[:pass])
            if User.find_by(email: email).nil?
                flash[:error] = "※ メールアドレスが存在しません。"
                redirect_to("/login")
            elsif User.find_by(email: email).pass != pass
                flash[:error] = "※ パスワードが正しくありません。"
                redirect_to("/login")
            else
                session[:user] = email
                redirect_to("/")
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
            email = params[:email]
            pass = Digest::SHA256.hexdigest(params[:pass])
            name = params[:name]
            if User.find_by(email: email)
                flash[:error] = "※ そのメールアドレスは重複のため使用できません。"
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
            Article.where(user: session[:user]).destroy_all
            User.find_by(email: session[:user]).destroy
            session.clear
            flash[:success] = "※ アカウント削除完了しました"
            redirect_to("/")
        else
            redirect_to("/login")
        end
    end

end
