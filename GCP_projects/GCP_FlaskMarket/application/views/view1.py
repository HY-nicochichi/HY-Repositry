from flask import Blueprint, render_template, redirect, request, flash, session
from application.helpers import SessionHelper, UserHelper, ItemHelper

bp1 = Blueprint('bp1', __name__, template_folder='../templates/temp1')

@bp1.get('/new_user')
def new_user_GET():
    if 'user' in session:
        flash('既にログイン済です')
        return redirect('/')
    user_info = {'login': False}
    return render_template('new_user.html', user_info=user_info)

@bp1.post('/new_user')
def new_user_POST():
    if 'user' in session:
        flash('既にログイン済です')
        return redirect('/')
    mail = request.form.get('mail', type=str)
    password = request.form.get('password', type=str)
    username = request.form.get('username', type=str)
    result = UserHelper.register(mail, password, username)
    if result['message'] == 'successed':
        SessionHelper.log_in(result['user_id'])
        return redirect('/')
    flash(result['message'])
    return redirect('/new_user')

@bp1.get('/delete_user')
def delete_user_GET():
    if 'user' not in session:
        return redirect('/login')
    ItemHelper.delete_by_seller(session['user'])
    UserHelper.delete(session['user'])
    SessionHelper.log_out()
    return redirect('/')

@bp1.get('/profile')
def profile_GET():
    if 'user' not in session:
        return redirect('/login')
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username,
        'mail': UserHelper.search_by_id(session['user']).mail
    }
    return render_template('profile.html', user_info=user_info)

@bp1.get('/update_profile')
def update_profile_GET():
    if 'user' not in session:
        return redirect('/login')
    param = request.args.get('param', type=str, default='default')
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username
    }
    return render_template('update_profile.html', user_info=user_info, param=param)

@bp1.post('/update_profile')
def update_profile_POST():
    if 'user' not in session:
        return redirect('/login')
    param = request.args.get('param', type=str, default='default')
    current_value = request.form.get(f'現{param}', type=str)
    new_value = request.form.get(f'新{param}', type=str)
    check_value = request.form.get(f'新{param}(確認)', type=str)
    if param == 'メールアドレス':
        result = UserHelper.update_mail(session['user'], current_value, new_value, check_value)
    elif param == 'パスワード':
        result = UserHelper.update_password(session['user'], current_value, new_value, check_value)
    elif param == 'ユーザーネーム':
        result = UserHelper.update_username(session['user'], current_value, new_value, check_value)
    if result == 'success':
        return redirect('/profile')
    flash(result)
    return redirect(f'/update_profile?param={param}')
