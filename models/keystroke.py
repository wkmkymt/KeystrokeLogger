# -*- coding: utf-8 -*-

from models import db


# ==================================================
#  Keystroke Model
# ==================================================

class Keystroke(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("user.id"))
    sentence_id  = db.Column(db.Integer, db.ForeignKey("sentence.id"))
    count        = db.Column(db.Integer)
    character    = db.Column(db.Unicode(1))
    press_time   = db.Column(db.Float)
    release_time = db.Column(db.Float)

    def __init__(self, user_id=None, sentence_id=None, count=None, character=None, press_time=None, release_time=None):
        self.user_id      = user_id
        self.sentence_id  = sentence_id
        self.count        = count
        self.character    = character
        self.press_time   = press_time
        self.release_time = release_time

    def __repr__(self):
        return "<Keystroke %d>" % self.id

    @classmethod
    def save(cls, *val):
        db.session.add(cls(*val))
        db.session.commit()

    @classmethod
    def getCreatCount(cls, user_id):
        stroke = db.session.query(cls).filter_by(user_id = user_id).order_by(cls.id.desc()).first()
        if stroke:
            return stroke.sentence_id
        else:
            return 1

    @classmethod
    def deleteAll(cls):
        db.session.query(cls).delete()
        db.session.commit()
