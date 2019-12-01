from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

from . import login_manager
from . import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    """
    This is class for users table and user model. the class also have methods for password generation
    and password authentication
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    full_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    blog = db.relationship('Blogs', backref = 'user', lazy = "dynamic")
    comment = db.relationship('Comments', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Blogs(db.Model):
    """docstring for Blogs."""

    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    blog = db.Column(db.String)
    published = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    comment = db.relationship('Comments', backref = 'blog', lazy = "dynamic")

    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        all_blogs = Blogs.query.all()

        return all_blogs

    @classmethod
    def get_single_blog(cls,id):
        single_blog = Blogs.query.filter_by(id = id).first()

        return single_blog


class Comments(db.Model):
    """docstring for Comments."""
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comments.query.filter_by(blog_id = blog_id).all()

    @classmethod
    def delete_comment(cls):
        pass
