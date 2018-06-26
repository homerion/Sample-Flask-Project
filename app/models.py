from app import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),index=True, unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(256))

    def __repr__(self):
        return 'Username= {}, Email = {}'.format(
        self.username,self.email)
