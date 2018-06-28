from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, RegisterForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post
from werkzeug.urls import url_parse


@app.route('/', methods=['GET','POST'])
@app.route('/index/', methods=['GET','POST'])
def index():
    user = {'username': 'Daniel'}
    num = 2+2
    return render_template('index.html', user=user,num=num,title='Home Page')

@app.route('/posts', methods=['GET','POST'])
@login_required
def posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.username.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Congratulations, on the new post!')
        return redirect(url_for('posts'))
    if current_user.is_authenticated:
        posts = current_user.posts
    else:
        posts=[]

    return render_template('posts.html',title='Posts',posts=posts,form=form)



# @app.route('/redirect')
# def goaway():
#     return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid login credentials')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        flash('Thanks for loggin in {}!'.format(current_user.username))
        return redirect(next_page)
    return render_template('login.html',form=login_form)


@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = User(username=register_form.username.data, \
            email=register_form.username.data)
        user.set_password(register_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))

    return render_template('register.html',form=register_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
