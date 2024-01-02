from flask import Blueprint, render_template, redirect, request, session, flash
from uuid import uuid4
from models1 import UserHelper
from models2 import ItemHelper

bp1 = Blueprint('bp1', __name__)

@bp1.route('/', methods=['GET'])
def index():
    user_info = {'login': False}
    if 'user' in session:
        user_info = {
            'login': True, 
            'name': UserHelper.search_by_id(session['user']).username
        }
    tag = request.args.get(key='tag', type=str, default='None')
    items = ItemHelper.tag_search(tag)
    itemList = []
    for item in items:
        itemList.append({
            'id': item.id,
            'name': item.itemname,
            'price': item.price
        })
    return render_template('index.html', user_info=user_info, items=itemList)

@bp1.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if 'user' in session:
        flash('既にログイン済です')
        return redirect('/')
    if request.method == 'POST':
        mail = request.form.get('mail', type=str)
        password = request.form.get('password', type=str)
        username = request.form.get('username', type=str)
        result = UserHelper.register(mail, password, username)
        if result['message'] == 'successed':
            session.sid = str(uuid4())
            session['user'] = result['userid']
            session['basket'] = {}
            return redirect('/')
        flash(result['message'])
        return redirect('/new_user')
    user_info = {'login': False}
    return render_template('new_user.html', user_info=user_info)

@bp1.route('/delete_user', methods=['GET'])
def delete_user():
    if 'user' not in session:
        return redirect('/login')
    state = request.args.get('state', type=str, default='default')
    if state == 'confirmed':
        ItemHelper.delete_by_seller(session['user'])
        UserHelper.delete(session['user'])
        session.clear()
        return redirect('/')
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username
    }
    return render_template('delete_user.html', user_info=user_info)

@bp1.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        flash('既にログイン済です')
        return redirect('/')
    if request.method == 'POST':
        mail = request.form.get('mail', type=str)
        password = request.form.get('password', type=str)
        result = UserHelper.auth(mail, password)
        if result['message'] == 'successed':
            session.sid = str(uuid4())
            session['user'] = result['userid']
            session['basket'] = {}
            return redirect('/')
        flash(result['message'])
        return redirect('/login')
    user_info = {'login': False}
    return render_template('login.html', user_info=user_info)

@bp1.route('/logout', methods=['GET'])
def logout():
    if 'user' not in session:
        return redirect('/login')
    session.clear()
    return redirect('/')

@bp1.route('/profile', methods=['GET'])
def profile():
    if 'user' not in session:
        return redirect('/login')
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username,
        'mail': UserHelper.search_by_id(session['user']).mail
    }
    return render_template('profile.html', user_info=user_info)

@bp1.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if 'user' not in session:
        return redirect('/login')
    param = request.args.get('param', type=str, default='default')
    if request.method == 'POST':
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
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username
    }
    return render_template('update_profile.html', user_info=user_info, param=param)
