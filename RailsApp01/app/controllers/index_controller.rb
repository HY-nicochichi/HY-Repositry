class IndexController < ActionController::Base

    # TOPページ
    def index
        if session[:user]
            @you = User.find_by(email: session[:user]).name
        else
            @you = "匿名"
        end
    end

end
