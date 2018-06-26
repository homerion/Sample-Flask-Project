from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegisterForm



@app.route('/', methods=['GET','POST'])
@app.route('/index/', methods=['GET','POST'])
def index():
    user = {'username': 'Daniel'}
    num = 2+2
    return render_template('index.html', user=user,num=num,title='Home Page')

@app.route('/posts')
def posts():
    posts=[
    'This is post #1',
    'This is post #2',
    'We\'re looping through these posts.',
    'This is Flask!'
    ]
    return render_template('posts.html',title='Posts',posts=posts)



# @app.route('/redirect')
# def goaway():
#     return redirect(url_for('index'))

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Thank you for logging in {}!'.format(login_form.username.data))
        return redirect(url_for('index'))

    return render_template('login.html',form=login_form)


@app.route('/register', methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        flash('Thank you for signing up {}!'.format(register_form.username.data))
        return redirect(url_for('index'))

    return render_template('register.html',form=register_form)
