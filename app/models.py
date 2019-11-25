from . import db

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
    
    def __repr__(self):
        return 'User {self.username}'
    