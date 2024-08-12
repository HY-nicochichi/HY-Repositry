class UserController < ApplicationController

  before_action :jwt_required, only: %i[info update delete]

  # POST "/api/user/create"
  def create()
    mail = params[:mail]
    password = params[:password]
    username = params[:username]
    found_user = User.find_by(mail: mail)
    if found_user
      return render(json: {msg: "メールアドレスの使用者が既に存在します"}, status: 401)
    else
      digestpass = Digest::SHA256.hexdigest(password)
      User.create(mail: mail, digestpass: digestpass, username: username)
      return render(json: {msg: "成功"}, status: 200)
    end
  end

  # GET "/api/user/info"
  def info()
    identity = get_jwt_identity()
    current_user = User.find_by(id: identity)
    if current_user
      return render(json: {user_info: {mail: current_user.mail, username: current_user.username}}, status: 200)
    else
      return render(json: {msg: "ユーザーが存在しません"}, status: 401)
    end
  end

  # POST "/api/user/update"
  def update()
    param = params[:param]
    current_value = params[:current_value]
    new_value = params[:new_value]
    check_value = params[:check_value]
    identity = get_jwt_identity()
    current_user = User.find_by(id: identity)
    if param == "メールアドレス"
      if current_user.mail != current_value
        return render(json: {msg: "現メールアドレスが誤っています"}, status: 401)
      elsif new_value != check_value
        return render(json: {msg: "新メールアドレスと確認用が一致しません"}, status: 401)
      elsif User.find_by(mail: new_value)
        return render(json: {msg: "新メールアドレスの使用者が既に存在します"}, status: 401)
      else
        current_user.mail = new_value
        current_user.save()
        return render(json: {msg: "成功"}, status: 200)
      end   
    elsif param == "パスワード"
      if current_user.digestpass != Digest::SHA256.hexdigest(current_value)
        return render(json: {msg: "現パスワードが誤っています"}, status: 401)
      elsif new_value != check_value
        return render(json: {msg: "新パスワードと確認用が一致しません"}, status: 401)
      else
        current_user.digestpass = Digest::SHA256.hexdigest(new_value)
        current_user.save()
        return render(json: {msg: "成功"}, status: 200)
      end
    else
      if current_user.username != current_value
        return render(json: {msg: "現ユーザーネームが誤っています"}, status: 401)
      elsif new_value != check_value
        return render(json: {msg: "新ユーザーネームと確認用が一致しません"}, status: 401)
      else
        current_user.username = new_value
        current_user.save()
        return render(json: {msg: "成功"}, status: 200)
      end
    end
  end

  # GET "/api/user/delete"
  def delete()
    identity = get_jwt_identity()
    current_user = User.find_by(id: identity)
    current_user.destroy()
    return render(json: {msg: "成功"}, status: 200)
  end

end
