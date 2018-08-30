# -*- coding: utf-8 -*-

from models import db


# ==================================================
#  Sentence Model
# ==================================================

class Sentence(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    text_k = db.Column(db.UnicodeText)
    text_r = db.Column(db.UnicodeText)

    def __init__(self, text_k=None, text_r=None):
        self.text_k = text_k
        self.text_r = text_r

    def __repr__(self):
        return "<Sentence %d>" % self.id

    @classmethod
    def save(cls, val):
        db.session.add(cls(*val))
        db.session.commit()

    @classmethod
    def getLast(cls):
        return db.session.query(cls).order_by(cls.id.desc()).first()
