from app import app
from flask import render_template, redirect,url_for




@app.route('/<name>', methods=['GET','PUT'])
@app.route('/index/<name>', methods=['GET','PUT'])
def index(name):
    user = {'username': 'Daniel'}
    num = 2+2
    return render_template('index.html', user=user,
    name=name,num=num,title='Home Page')

@app.route('/posts')
def posts():
    posts=[
    'This is post #1',
    'This is post #2',
    'We\'re looping through these posts.',
    'This is Flask!'
    ]
    return render_template('posts.html',title='Posts',posts=posts)

@app.route('/redirect')
def goaway():
    return redirect(url_for('index'))
