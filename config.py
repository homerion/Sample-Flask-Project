import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#you will never guess should be a huge psudorandom string
#DO NOT USE THE SECRET KEY ON GITHUB

# app.config['SECRET_KEY']= 'you-will-never-guess'
