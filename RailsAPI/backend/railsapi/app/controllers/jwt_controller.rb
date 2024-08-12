class JwtController < ApplicationController

  # POST "/api/jwt/create"
  def create()
    mail = params[:mail]
    password = params[:password]
    found_user = User.find_by(mail: mail)
    if !found_user
      return render(json: {msg: "メールアドレスが存在しません"}, status: 401)
    elsif Digest::SHA256.hexdigest(password) != found_user.digestpass
      return render(json: {msg: "パスワードが誤っています"}, status: 401)
    else
      identity = found_user.id
      access_token = create_access_token(identity)
      return render(json: {access_token: access_token}, status: 200)
    end
  end

end
