module UsersHelper

    def auth(email, pass)
        result = {}
        found_user = search_by_email(email)
        if found_user.nil?()
            result["message"] = "※ ユーザーが存在しません"
        elsif Digest::SHA256.hexdigest(pass) != found_user.pass
            result["message"] = "※ パスワードが誤っています"
        else
            result["message"] = "successed"
            result["user_id"] = found_user.id
        end
        return result
    end

    def search_by_id(id)
        found_user = User.find_by(id: id)
        return found_user
    end
    
    def search_by_email(email)
        found_user = User.find_by(email: email)
        return found_user
    end

    def register(email, pass, name)
        result = {}
        if search_by_email(email)
            result["message"] = "※ メールアドレスの使用者が既に存在します"
        else
            digestPASS = Digest::SHA256.hexdigest(pass)
            User.create(email: email, pass: digestPASS, name: name)
            result["message"] = "successed"
            result["user_id"] = search_by_email(email).id
        end
        return result
    end

    def delete(id)
        search_by_id(id).destroy()
    end

    def update_email(id, current_email, new_email, check_email)
        user = search_by_id(id)
        if user.email != current_email
            result = "※ 現メールアドレスが誤っています"
        elsif new_email != check_email
            result = "※ 新メールアドレスと確認用が一致しません"
        elsif search_by_email(new_email)
            result = "※ 新メールアドレスの使用者が既に存在します"
        else
            user.update(email: new_email, pass: user.pass, name: user.name)
            result = "success"
        end 
        return result
    end
    
    def update_pass(id, current_pass, new_pass, check_pass)
        user = search_by_id(id)
        if Digest::SHA256.hexdigest(current_pass) != user.pass
            result = "※ 現パスワードが誤っています"
        elsif new_pass != check_pass
            result = "※ 新パスワードと確認用が一致しません"
        else
            user.update(email: user.email, pass: Digest::SHA256.hexdigest(new_pass), name: user.name)
            result = "success"
        end
        return result
    end

    def update_name(id, current_name, new_name, check_name)
        user = search_by_id(id)
        if user.name != current_name
            result = "※ 現ユーザーネームが誤っています"
        elsif new_name != check_name
            result = "※ 新ユーザーネームと確認用が一致しません"
        else
            user.update(email: user.email, pass: user.pass, name: new_name)
            result = "success"
        end
        return result
    end

end
