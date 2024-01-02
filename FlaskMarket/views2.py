from flask import Blueprint, render_template, redirect, request, session
from models1 import UserHelper
from models2 import ItemHelper

bp2 = Blueprint('bp2', __name__)

@bp2.route('/new_item', methods=['GET', 'POST'])
def new_item():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        itemname = request.form.get('itemname', type=str)
        price = request.form.get('price', type=int)
        stock = request.form.get('stock', type=int)
        tag = request.form.get('tag', type=str)
        seller = session['user']
        ItemHelper.register(itemname, price, stock, tag, seller)
        return redirect('/')
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username
    }
    return render_template('new_item.html', user_info=user_info)

@bp2.route('/description', methods=['GET', 'POST'])
def description():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        item = request.form.get('item', type=str)
        session['basket'][item] = 1
        return redirect('/')
    id = request.args.get(key='id', type=str)
    item = ItemHelper.search_by_id(id)
    seller = UserHelper.search_by_id(item.seller)
    description = {
        'id': id,
        'name': item.itemname,
        'price': item.price,
        'stock': item.stock,
        'seller': seller.username,
        'in_basket': id in session['basket']
    }
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username
    }
    return render_template('description.html', user_info=user_info, description=description)

@bp2.route('/basket', methods=['GET', 'POST'])
def basket():
    if 'user' not in session:
        return redirect('/login')
    basket = {'content': [], 'sum': 0}
    if request.method == 'POST':
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
    for key in list(session['basket'].keys()):
        item = ItemHelper.search_by_id(key)
        if item == None:
            del session['basket'][key]
        else:
            basket['content'].append({'id': key, 'name': item.itemname, 
            'num': session['basket'][key], 'stock': item.stock, 'price': item.price})
            basket['sum'] += session['basket'][key] * item.price
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username
    }
    return render_template('basket.html', user_info=user_info, basket=basket)

@bp2.route('/update_items', methods=['GET', 'POST'])
def update_items():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        id = request.form.get('id', type=str)
        price = request.form.get('price', type=int)
        stock = request.form.get('stock', type=int)
        ItemHelper.update_price(id, price)
        ItemHelper.update_stock(id, stock)
        return redirect('/update_items')
    state = request.args.get('state', type=str, default='default')
    if state == 'delete':
        del_id = request.args.get('del_id', type=str)
        ItemHelper.delete_by_id(del_id)
        return redirect('/update_items')
    user_info = {
        'login': True, 
        'name': UserHelper.search_by_id(session['user']).username
    }
    items = ItemHelper.seller_search(session['user'])
    itemList = []
    for item in items:
        itemList.append({
            'id': item.id,
            'name': item.itemname,
            'price': item.price,
            'stock': item.stock
        })
    return render_template('update_items.html', user_info=user_info, items=itemList)
