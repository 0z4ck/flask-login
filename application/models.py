# -*- coding: utf-8 -*-
from database import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(10))
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username, password, d=1):
        self.username = username
        self.password = password
        self.registered_on = datetime.now()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def __repr__(self):
        return '<User %r>' % (self.username)
