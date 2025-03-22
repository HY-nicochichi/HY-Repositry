class ApplicationController < ActionController::Base
  
  def check_login_user
    @user = User.find_by(id: session[:user_id])
    if @user.nil?()
      reset_session()
      flash[:danger] = "ログインしてください"
      return redirect_to(session_new_path, status: :see_other)
    end
  end

end
