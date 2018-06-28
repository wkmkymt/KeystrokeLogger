# -*- coding: utf-8 -*-

from models import db


# ==================================================
#  Keystroke Model
# ==================================================

class Keystroke(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("user.id"))
    target_id    = db.Column(db.Integer, db.ForeignKey("user.id"))
    character    = db.Column(db.Unicode(1))
    press_time   = db.Column(db.DateTime)
    release_time = db.Column(db.DateTime)

    def __init__(self, user_id=None, target_id=None, character=None, press_time=None, release_time=None):
        self.user_id      = user_id
        self.target_id    = target_id
        self.character    = character
        self.press_time   = press_time
        self.release_time = release_time

    def __repr__(self):
        return "<Keystroke %d>" % self.id

    @classmethod
    def save(cls, val):
        db.session.add(cls(*val))
        db.session.commit()
