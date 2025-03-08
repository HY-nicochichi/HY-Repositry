class UserController < ApplicationController

  # /user/

  def get()
    result = current_user_or_error_response()
    current_user = result[:user]
    if current_user == nil
      return result[:response]
    else
      return render(json: {mail: current_user.mail, name: current_user.name}, status: 200)
    end
  end

  def post()
    mail = params[:mail]
    password = params[:password]
    name = params[:name]
    found_user = User.find_by(mail: mail)
    if found_user
      return render(json: {msg: "メールアドレスの使用者が既に存在します"}, status: 409)
    else
      digestpass = Digest::SHA256.hexdigest(password)
      User.create(mail: mail, digestpass: digestpass, name: name)
      return render(json: {msg: "登録しました"}, status: 200)
    end
  end

  def put()
    param = params[:param]
    current_val = params[:current_val]
    new_val = params[:new_val]
    check_val = params[:check_val]
    result = current_user_or_error_response()
    current_user = result[:user]
    if current_user == nil
      return result[:response]
    else
      if param == "メールアドレス"
        if current_user.mail != current_val
          return render(json: {msg: "現メールアドレスが誤っています"}, status: 404)
        elsif new_val != check_val
          return render(json: {msg: "新メールアドレスと確認用が一致しません"}, status: 422)
        elsif User.find_by(mail: new_val)
          return render(json: {msg: "新メールアドレスの使用者が既に存在します"}, status: 409)
        else
          current_user.mail = new_val
          current_user.save()
          return render(json: {msg: "メールアドレスを変更しました"}, status: 200)
        end   
      elsif param == "パスワード"
        if current_user.digestpass != Digest::SHA256.hexdigest(current_val)
          return render(json: {msg: "現パスワードが誤っています"}, status: 404)
        elsif new_val != check_val
          return render(json: {msg: "新パスワードと確認用が一致しません"}, status: 422)
        else
          current_user.digestpass = Digest::SHA256.hexdigest(new_val)
          current_user.save()
          return render(json: {msg: "パスワードを変更しました"}, status: 200)
        end
      else
        if current_user.name != current_val
          return render(json: {msg: "現ユーザーネームが誤っています"}, status: 404)
        elsif new_val != check_val
          return render(json: {msg: "新ユーザーネームと確認用が一致しません"}, status: 422)
        else
          current_user.name = new_val
          current_user.save()
          return render(json: {msg: "ユーザーネームを変更しました"}, status: 200)
        end
      end
    end
  end

  def delete()
    result = current_user_or_error_response()
    current_user = result[:user]
    if current_user == nil
      return result[:response]
    else
      current_user.destroy()
      return render(json: {msg: "退会しました"}, status: 200)
    end
  end

end
