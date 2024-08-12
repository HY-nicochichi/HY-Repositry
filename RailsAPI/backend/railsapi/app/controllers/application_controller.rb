class ApplicationController < ActionController::API

  def jwt_required()
    authorization_header = request.headers[:authorization]
    if !authorization_header
      return render(json: {msg: "Missing Authorization Header"}, status: 401)
    elsif authorization_header.split(" ").size != 2 || authorization_header.split(" ")[0] != "Bearer"
      return render(json: {msg: "Expected 'Authorization: Bearer <JWT>'"}, status: 422)
    else
      token = authorization_header.split(" ")[1]
      secret_key = Rails.application.credentials.secret_key_base
      begin
        _ = JWT.decode(token, secret_key, true, {algorithm: "HS256"})
      rescue JWT::DecodeError
        return render(json: {msg: "Unsuccessful JWT Decode"}, status: 422)
      rescue JWT::ExpiredSinature
        return render(json: {msg: "Token Expired"}, status: 422)
      rescue StandardError
        return render(json: {msg: "Token Invalid"}, status: 422)
      end
    end
  end

  def get_jwt_identity()
    token = request.headers[:authorization].split(" ")[1]
    secret_key = Rails.application.credentials.secret_key_base
    payload = JWT.decode(token, secret_key, true, {algorithm: "HS256"})[0]
    identity = payload["identity"]  # 注意！ payload[:identity]はダメ！
    return identity
  end

  def create_access_token(identity)
    expires = Time.now.to_i + 7*24*60*60
    payload = {identity: identity, exp: expires}
    secret_key = Rails.application.credentials.secret_key_base
    access_token = JWT.encode(payload, secret_key, "HS256")
    return access_token
  end

end
