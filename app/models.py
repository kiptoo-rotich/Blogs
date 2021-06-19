from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class User(UserMixin,db.Model):
    '''
    '''
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    password_secure=db.Column(db.String(255))
    location=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password atribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User{self.username}'

class Quotes:
    '''
    This is a class to define news details objects
    '''
    def __init__(self,id, quote,author):
        self.id = id
        self.quote=quote
        self.author=author