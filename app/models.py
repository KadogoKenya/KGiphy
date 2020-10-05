from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager




class Giphy:
    '''
    Food class to define the Food obajects available.
    '''

    def __init__(self,id,url,title,images):

        self.id=id
        self.url=url
        self.title=title
        self.images=images


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    email = db.Column(db.String(255),unique = True,index = True)
    
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    

    def __repr__(self):
        return f'User {self.name}'
        comment = db.Column(db.Text(),nullable = False)
        users = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
        role_id = db.Column(db.Integer,db.ForeignKey('roles.id'),nullable = False)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))