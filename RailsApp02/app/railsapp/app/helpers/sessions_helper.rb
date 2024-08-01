module SessionsHelper

    def log_in(user_id)
        reset_session()
        session["user"] = user_id
    end

    def log_out()
        reset_session()
    end

end
