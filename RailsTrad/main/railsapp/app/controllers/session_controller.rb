class SessionController < ApplicationController

  before_action(:check_login_user, only: [:destroy])

  # GET /session/new
  def new
  end

  # POST /session/create
  def create
    user = User.find_by(mail: params[:mail].downcase())
    if user && user.correct_password?(params[:password])
      reset_session()
      session[:user_id] = user.id
      return redirect_to(root_path, status: :see_other)
    else
      flash[:danger] = "メールアドレスかパスワードに誤りがあります"
      return redirect_to(session_new_path, status: :see_other)
    end
  end

  # DELETE /session/destroy
  def destroy
    reset_session()
    return redirect_to(root_path, status: :see_other)
  end

end
