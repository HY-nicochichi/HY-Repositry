class ApplicationController < ActionController::API

  def current_user_or_error_response()
    result = {user: nil, response: nil}
    authorization_header = request.headers[:authorization]
    if !authorization_header
      result[:response] = render(json: {msg: "Authorizationヘッダがありません"}, status: 401)
    else 
      split = authorization_header.split(" ")
      if split.size != 2 || split[0] != "Bearer"
        result[:response] = render(json: {msg: "Authorizationヘッダの値が'Bearer JWT'と異なります"}, status: 422)
      else
        token = split[1]
        secret_key = Rails.application.credentials.secret_key_base
        begin
          payload = JWT.decode(token, secret_key, true, {algorithm: "HS256"})[0]
        rescue JWT::DecodeError
          result[:response] = render(json: {msg: "JWTの解読に失敗しました"}, status: 422)
        rescue JWT::ExpiredSignature
          result[:response] = render(json: {msg: "JWTが期限切れです"}, status: 401)
        rescue StandardError
          result[:response] = render(json: {msg: "JWTが無効です"}, status: 400)
        end
        identity = payload["identity"]  # payload[:identity]はダメ
        current_user = User.find_by(id: identity)
        if current_user == nil
          result[:response] = render(json: {msg: "JWTデータに対応するユーザーがありません"}, status: 401)
        else
          result[:user] = current_user
        end
      end
    end
    return result
  end

  def create_access_token(identity)
    expires = Time.now().to_i() + 7*24*60*60
    payload = {identity: identity, exp: expires}
    secret_key = Rails.application.credentials.secret_key_base
    access_token = JWT.encode(payload, secret_key, "HS256")
    return access_token
  end

end
