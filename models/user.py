# -*- coding: utf-8 -*-

from models import db


# ==================================================
#  User Model
# ==================================================

class User(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Unicode(30))
    last_name  = db.Column(db.Unicode(30))
    school_id  = db.Column(db.Unicode(6))
    city_name  = db.Column(db.Unicode(30))
    keystrokes = db.relationship("Keystroke", backref="user", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, first_name, last_name, school_id, city_name):
        self.first_name = first_name
        self.last_name  = last_name
        self.school_id  = school_id
        self.city_name  = city_name

    def __repr__(self):
        return "<User %d>" % self.id

    @classmethod
    def save(cls, val):
        db.session.add(cls(*val))
        db.session.commit()
