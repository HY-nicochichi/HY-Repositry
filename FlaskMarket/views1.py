from flask import Blueprint, render_template, redirect, request, session, flash
from models1 import User

bp1 = Blueprint('bp1', __name__)

@bp1.route('/', methods=['GET'])
def index():
    yourname = '未ログイン'
    if 'user'  in session:
        yourname = User.search_by_id(session['user']).username
    return render_template('index.html', yourname=yourname)

@bp1.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        mail = request.form.get('MAIL', type=str)
        password = request.form.get('PASS', type=str)
        username = request.form.get('username', type=str)
        result = User.register(mail, password, username)
        if result['message'] == 'successed':
            session.clear()
            session['user'] = result['userid']
            session['cart'] = {}
            session.permanent = True
            return redirect('/')
        flash(result['message'])
        return redirect('/signup')
    return render_template('signup.html')

@bp1.route('/signout', methods=['GET'])
def signout():
    if 'user' not in session:
        return redirect('/login')
    state = request.args.get('state', type=str, default='default')
    if state == 'confirmed':
        User.delete(session['user'])
        session.clear()
        return redirect('/')
    else:
        return render_template('signout.html')

@bp1.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mail = request.form.get('MAIL', type=str)
        password = request.form.get('PASS', type=str)
        result = User.auth(mail, password)
        if result['message'] == 'successed':
            session.clear()
            session['user'] = result['userid']
            session['cart'] = {}
            session.permanent = True
            return redirect('/')
        flash(result['message'])
        return redirect('/login')
    return render_template('login.html')

@bp1.route('/logout', methods=['GET'])
def logout():
    if 'user' not in session:
        return redirect('/login')
    session.clear()
    return redirect('/')
