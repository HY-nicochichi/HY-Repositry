class RootController < ApplicationController

  # GET /
  def index
    @user = User.find_by(id: session[:user_id])
    if @user.nil?()
      reset_session()
    end
  end

end
