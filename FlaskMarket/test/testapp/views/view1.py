from flask import Blueprint, jsonify, redirect, request, session
from helpers import SessionHelper, UserHelper, ItemHelper
from json import loads

bp1 = Blueprint('bp1', __name__)

@bp1.get('/new_user')
def new_user_GET():
    if 'user' in session:
        current_user = UserHelper.search_by_id(session['user'])
        if current_user == None:
            SessionHelper.log_out()
            return redirect('/new_user')
        return redirect('/')
    user_info = {'login': False}
    resDict = {'user_info': user_info}
    return jsonify(resDict)

@bp1.post('/new_user')
def new_user_POST():
    if 'user' in session:
        current_user = UserHelper.search_by_id(session['user'])
        if current_user:
            return redirect('/')
        else:
            SessionHelper.log_out()
    mail = request.form('mail', type=str)
    password = request.form('password', type=str)
    username = request.form('username', type=str)
    result = UserHelper.register(mail, password, username)
    if result['message'] == 'successed':
        SessionHelper.log_in(result['user_id'])
        return redirect('/')
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
    current_user = UserHelper.search_by_id(session['user'])
    if current_user == None:
        SessionHelper.log_out()
        return redirect('/login')
    user_info = {
        'login': True, 
        'name': current_user.username,
        'mail': current_user.mail
    }
    resDict = {'user_info': user_info}
    return jsonify(resDict)

@bp1.get('/update_profile')
def update_profile_GET():
    if 'user' not in session:
        return redirect('/login')
    current_user = UserHelper.search_by_id(session['user'])
    if current_user == None:
        SessionHelper.log_out()
        return redirect('/login')
    user_info = {
        'login': True, 
        'name': current_user.username
    }
    param = request.args.get('param', type=str, default='default')
    resDict = {'user_info': user_info, 'param': param}
    return jsonify(resDict)

@bp1.post('/update_profile')
def update_profile_POST():
    if 'user' not in session:
        return redirect('/login')
    current_user = UserHelper.search_by_id(session['user'])
    if current_user == None:
        SessionHelper.log_out()
        return redirect('/login')
    param = request.args.get('param', type=str, default='default')
    current_value = request.form(f'現{param}', type=str)
    new_value = request.form(f'新{param}', type=str)
    check_value = request.form(f'新{param}(確認)', type=str)
    if param == 'メールアドレス':
        result = UserHelper.update_mail(session['user'], current_value, new_value, check_value)
    elif param == 'パスワード':
        result = UserHelper.update_password(session['user'], current_value, new_value, check_value)
    elif param == 'ユーザーネーム':
        result = UserHelper.update_username(session['user'], current_value, new_value, check_value)
    if result == 'success':
        return redirect('/profile')
    return redirect(f'/update_profile?param={param}')
