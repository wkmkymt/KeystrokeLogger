# -*- coding: utf-8 -*-

from models import db


# ==================================================
#  Sentence Model
# ==================================================

class Sentence(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.UnicodeText)

    def __init__(self, sentence):
        self.sentence = sentence
        
    def __repr__(self):
        return "<Sentence %d>" % self.id

    @classmethod
    def save(cls, val):
        db.session.add(cls(*val))
        db.session.commit()
