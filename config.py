import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = \
    os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


#you will never guess should be a huge psudorandom string
#DO NOT USE THE SECRET KEY ON GITHUB

# app.config['SECRET_KEY']= 'you-will-never-guess'
