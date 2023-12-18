from flask import Blueprint, render_template, redirect, request, session
from models2 import Item

bp2 = Blueprint('bp2', __name__)

@bp2.route('/new_item', methods=['GET', 'POST'])
def new_item():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        itemname = request.form.get('NAME', type=str)
        price = request.form.get('PRICE', type=int)
        stock = request.form.get('STOCK', type=int)
        tag = request.form.get('TAG', type=str)
        seller = session['user']
        Item.register(itemname, price, stock, tag, seller)
        return redirect('/items')
    return render_template('new_item.html')

@bp2.route('/items', methods=['GET'])
def items():
    tag = request.args.get(key='TAG', type=str, default='None')
    results = Item.tag_search(tag)
    return render_template('items.html', results=results)

@bp2.route('/description', methods=['GET', 'POST'])
def description():
    if request.method == 'POST':
        if 'user' not in session:
            return redirect('/login')
        item = request.form.get('ITEM', type=str)
        session['cart'][item] = 1
        return redirect('/items')
    else:
        id = request.args.get(key='id', type=str)
        item = Item.search_by_id(id)
        description = {
            'id': id,
            'name': item.itemname,
            'price': item.price,
            'stock': item.stock,
            'incart': 'user' in session and id in session['cart']
        }
    return render_template('description.html', description=description)

@bp2.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart():
    if 'user' not in session:
        return redirect('/login')
    cart = []
    sum = 0
    if request.method == 'POST':
        for key in list(session['cart'].keys()):
            session['cart'][key] = request.form.get(key, type=int)
            if session['cart'][key] == 0 or Item.search_by_id(key) == None:
                del session['cart'][key]
        if request.form.get('ACT', type=str) == 'order':
            for key in session['cart']:
                new_stock = Item.search_by_id(key).stock - session['cart'][key]
                Item.update_stock(key, new_stock)
            session['cart'].clear()
        return redirect('/shopping_cart')
    for key in list(session['cart'].keys()):
        item = Item.search_by_id(key)
        if item == None:
            del session['cart'][key]
        else:
            cart.append({'id': key, 'name': item.itemname, 
            'num': session['cart'][key], 'stock': item.stock, 'price': item.price})
            sum += session['cart'][key] * item.price
    return render_template('shopping_cart.html', cart=cart, sum=sum)

@bp2.route('/update_items', methods=['GET', 'POST'])
def update_items():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        id = request.form.get('ID', type=str)
        if request.form.get('ACT', type=str) == 'delete':
            Item.delete_by_id(id)
        else:
            price = request.form.get('PRICE', type=int)
            stock = request.form.get('STOCK', type=int)
            Item.update_price(id, price)
            Item.update_stock(id, stock)
        return redirect('/update_items')
    items = Item.seller_search(session['user'])
    return render_template('update_items.html', items=items)
