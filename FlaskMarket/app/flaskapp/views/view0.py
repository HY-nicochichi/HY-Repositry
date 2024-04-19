from flask import Blueprint, render_template, redirect, request, flash, session
from helpers import SessionHelper, UserHelper, ItemHelper

bp0 = Blueprint('bp0', __name__, template_folder='../templates/temp0')

@bp0.get('/')
def index_GET():
    user_info = {'login': False}
    if 'user' in session:
        current_user = UserHelper.search_by_id(session['user'])
        if current_user == None:
            SessionHelper.log_out()
            return redirect('/')
        user_info = {
            'login': True, 
            'name': current_user.username
        }
    tag = request.args.get(key='tag', type=str, default='None')
    items = ItemHelper.tag_search(tag)
    itemList = []
    for item in items:
        itemList.append({
            'item_id': item.item_id,
            'name': item.itemname,
            'price': item.price
        })
    return render_template('index.html', user_info=user_info, items=itemList)

@bp0.get('/login')
def login_GET():
    if 'user' in session:
        current_user = UserHelper.search_by_id(session['user'])
        if current_user == None:
            SessionHelper.log_out()
            return redirect('/login')
        flash('既にログイン済です')
        return redirect('/')
    user_info = {'login': False}
    return render_template('login.html', user_info=user_info)

@bp0.post('/login')
def login_POST():
    if 'user' in session:
        current_user = UserHelper.search_by_id(session['user'])
        if current_user == None:
            SessionHelper.log_out()
            flash('ユーザーが存在しません')
            return redirect('/login')
        flash('既にログイン済です')
        return redirect('/')
    mail = request.form.get('mail', type=str)
    password = request.form.get('password', type=str)
    result = UserHelper.auth(mail, password)
    if result['message'] == 'successed':
        SessionHelper.log_in(result['user_id'])
        return redirect('/')
    flash(result['message'])
    return redirect('/login')

@bp0.get('/logout')
def logout_GET():
    if 'user' not in session:
        return redirect('/login')
    SessionHelper.log_out()
    return redirect('/')
