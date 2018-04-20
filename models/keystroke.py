# -*- coding: utf-8 -*-

from models import db


# ==================================================
#  Keystroke Model
# ==================================================

class Keystroke(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    def __init__(self):
        pass


    def __repr__(self):
        return "<Keystroke %d>" % self.id
