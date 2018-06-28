# -*- coding: utf-8 -*-

from flask_login import UserMixin

from models import db


# ==================================================
#  User Model
# ==================================================

class User(db.Model, UserMixin):
    id      = db.Column(db.Integer, primary_key=True)
    tokens  = db.Column(db.Unicode(200))
    email   = db.Column(db.Unicode(30))
    fname_k = db.Column(db.Unicode(30))
    lname_k = db.Column(db.Unicode(30))
    fname_r = db.Column(db.Unicode(30))
    lname_r = db.Column(db.Unicode(30))

    def __init__(self, tokens=None, email=None, lname_k=None, fname_k=None, lname_r=None, fname_r=None):
        self.tokens  = tokens
        self.email   = email
        self.lname_k = lname_k
        self.fname_k = fname_k
        self.lname_r = lname_r
        self.fname_r = fname_r

    def __repr__(self):
        return "<User: %s %s>" % (self.lname_k, self.fname_k)

    @classmethod
    def save(cls, user):
        db.session.add(user)
        db.session.commit()
