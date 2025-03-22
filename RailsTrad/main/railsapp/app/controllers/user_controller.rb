class UserController < ApplicationController

  before_action(:check_login_user, only: [:show, :edit, :update, :destroy])

  # GET /user/show
  def show
  end

  # GET /user/new
  def new
  end

  # GET /user/edit?param=ユーザーネーム
  def edit
    @param = params[:param]
    unless ["メールアドレス", "パスワード", "ユーザーネーム"].include?(@param)
      flash[:danger] = "変更可能な項目はメールアドレス・パスワード・ユーザーネームです"
      return redirect_to(user_edit_path(param: "ユーザーネーム"), status: :see_other)
    end
  end

  # POST /user/create
  def create
    mail = params[:mail]
    if User.find_by(mail: mail)
      flash[:danger] = "メールアドレスの使用者が既に存在します"
      return redirect_to(user_new_path, status: :see_other)
    else
      password_enc = User.enc_val(params[:password])
      name = params[:name]
      user = User.create(mail: mail, password_enc: password_enc, name: name)
      reset_session()
      session[:user_id] = user.id
      return redirect_to(root_path, status: :see_other) 
    end
  end

  # PUT /user/update
  def update
    param = params[:param]
    current_val = params[:current_val]
    new_val = params[:new_val]
    check_val = params[:check_val]
    if param == "メールアドレス"
      if @user.mail != current_val
        flash[:danger] = "現メールアドレスが誤っています"
        return redirect_to(user_edit_path(param: "メールアドレス"), status: :see_other)
      elsif new_val != check_val
        flash[:danger] = "新メールアドレスと確認用が一致しません"
        return redirect_to(user_edit_path(param: "メールアドレス"), status: :see_other)
      elsif User.find_by(mail: new_val)
        flash[:danger] = "新メールアドレスの使用者が既に存在します"
        return redirect_to(user_edit_path(param: "メールアドレス"), status: :see_other)
      else
        @user.mail = new_val
        @user.save()
        return redirect_to(user_show_path, status: :see_other)
      end   
    elsif param == "パスワード"
      if @user.correct_password?(current_val) == false
        flash[:danger] = "現パスワードが誤っています"
        return redirect_to(user_edit_path(param: "パスワード"), status: :see_other)
      elsif new_val != check_val
        flash[:danger] = "新パスワードと確認用が一致しません"
        return redirect_to(user_edit_path(param: "パスワード"), status: :see_other)
      else
        @user.password_enc = User.enc_val(new_val)
        @user.save()
        return redirect_to(user_show_path, status: :see_other)
      end
    else
      if @user.name != current_val
        flash[:danger] = "現ユーザーネームが誤っています"
        return redirect_to(user_edit_path(param: "ユーザーネーム"), status: :see_other)
      elsif new_val != check_val
        flash[:danger] = "新ユーザーネームと確認用が一致しません"
        return redirect_to(user_edit_path(param: "ユーザーネーム"), status: :see_other)
      else
        @user.name = new_val
        @user.save()
        return redirect_to(user_show_path, status: :see_other)
      end
    end
  end

  # DELETE /user/destroy
  def destroy
    User.find_by(id: session[:user_id]).destroy()
    reset_session()
    redirect_to(root_path, status: :see_other)
  end

end
