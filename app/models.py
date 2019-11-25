from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Comment(db.Model):
    __tablename__ = 'comments' 
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref ='comment',lazy="dynamic") 
    def __repr__(self):
        return 'User {self.name}'
    
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    pass_secure = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return 'User {self.username}'
    