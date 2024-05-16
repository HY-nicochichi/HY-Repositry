from flask import Blueprint, jsonify, redirect, request, session
from helpers import SessionHelper, UserHelper, ItemHelper

bp0 = Blueprint('bp0', __name__)

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
    resDict = {'user_info': user_info, 'items': itemList}
    return jsonify(resDict)

@bp0.get('/login')
def login_GET():
    if 'user' in session:
        current_user = UserHelper.search_by_id(session['user'])
        if current_user == None:
            SessionHelper.log_out()
            return redirect('/login')
        return redirect('/')
    user_info = {'login': False}
    resDict = {'user_info': user_info}
    return jsonify(resDict)

@bp0.post('/login')
def login_POST():
    if 'user' in session:
        current_user = UserHelper.search_by_id(session['user'])
        if current_user == None:
            SessionHelper.log_out()
            return redirect('/login')
        return redirect('/')
    mail = request.form.get('mail', type=str)
    password = request.form.get('password', type=str)
    result = UserHelper.auth(mail, password)
    if result['message'] == 'successed':
        SessionHelper.log_in(result['user_id'])
        return redirect('/')
    return redirect('/login')

@bp0.get('/logout')
def logout_GET():
    if 'user' not in session:
        return redirect('/login')
    SessionHelper.log_out()
    return redirect('/')
