from flask import Blueprint, jsonify, redirect, request, session
from helpers import SessionHelper, UserHelper, ItemHelper

bp2 = Blueprint('bp2', __name__)

@bp2.get('/new_item')
def new_item_GET():
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
    resDict = {'user_info': user_info}
    return jsonify(resDict)

@bp2.post('/new_item')
def new_item_POST():
    if 'user' not in session:
        return redirect('/login')
    current_user = UserHelper.search_by_id(session['user'])
    if current_user == None:
        SessionHelper.log_out()
        return redirect('/login')
    itemname = request.form.get('itemname', type=str)
    price = request.form.get('price', type=int)
    stock = request.form.get('stock', type=int)
    tag = request.form.get('tag', type=str)
    seller = session['user']
    ItemHelper.register(itemname, price, stock, tag, seller)
    return redirect('/')

@bp2.get('/description')
def description_GET():
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
    item_id = request.args.get(key='item_id', type=str)
    item = ItemHelper.search_by_id(item_id)
    seller = UserHelper.search_by_id(item.seller)
    description = {
        'item_id': item_id,
        'name': item.itemname,
        'price': item.price,
        'stock': item.stock,
        'seller': seller.username,
        'in_basket': item_id in session['basket']
    }
    resDict = {'user_info': user_info, 'description': description}
    return jsonify(resDict)

@bp2.post('/description')
def description_POST():
    if 'user' not in session:
        return redirect('/login')
    current_user = UserHelper.search_by_id(session['user'])
    if current_user == None:
        SessionHelper.log_out()
        return redirect('/login')
    item_id = request.form.get('item_id', type=str)
    session['basket'][item_id] = 1
    return redirect('/')

@bp2.get('/basket')
def basket_GET():
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
    basket = []
    for key in list(session['basket'].keys()):
        item = ItemHelper.search_by_id(key)
        if item == None:
            del session['basket'][key]
        else:
            basket.append({'item_id': key, 'name': item.itemname, 
            'num': session['basket'][key], 'stock': item.stock, 'price': item.price})
    resDict = {'user_info': user_info, 'basket': basket}
    return jsonify(resDict)

@bp2.post('/basket')
def basket_POST():
    if 'user' not in session:
        return redirect('/login')
    current_user = UserHelper.search_by_id(session['user'])
    if current_user == None:
        SessionHelper.log_out()
        return redirect('/login')
    for key in list(session['basket'].keys()):
        session['basket'][key] = request.form.get(key, type=int)
        if session['basket'][key] == 0 or ItemHelper.search_by_id(key) == None:
            del session['basket'][key]
    if request.form.get('act', type=str) == 'order':
        for key in session['basket']:
            new_stock = ItemHelper.search_by_id(key).stock - session['basket'][key]
            ItemHelper.update_stock(key, new_stock)
        session['basket'].clear()
    return redirect('/basket')

@bp2.get('/update_items')
def update_items_GET():
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
    state = request.args.get('state', type=str, default='default')
    if state == 'delete':
        del_id = request.args.get('del_id', type=str)
        ItemHelper.delete_by_id(del_id)
        return redirect('/update_items')
    items = ItemHelper.seller_search(session['user'])
    itemList = []
    for item in items:
        itemList.append({
            'item_id': item.item_id,
            'name': item.itemname,
            'price': item.price,
            'stock': item.stock
        })
    resDict = {'user_info': user_info, 'items': itemList}
    return jsonify(resDict)

@bp2.post('/update_items')
def update_items_POST():
    if 'user' not in session:
        return redirect('/login')
    current_user = UserHelper.search_by_id(session['user'])
    if current_user == None:
        SessionHelper.log_out()
        return redirect('/login')
    item_id = request.form.get('item_id', type=str)
    price = request.form.get('price', type=int)
    stock = request.form.get('stock', type=int)
    ItemHelper.update_price(item_id, price)
    ItemHelper.update_stock(item_id, stock)
    return redirect('/update_items')
