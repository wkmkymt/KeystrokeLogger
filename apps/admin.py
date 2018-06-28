# -*- coding: utf-8 -*-

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app
from models import db, Keystroke, User


# ==================================================
#  Keystroke Views
# ==================================================

# class MyKeystrokeView(ModelView):
#     column_list = ("id", "name", "Q1", "Q2", "Q3", "Q4", "Q5")


# ==================================================
#  Initialize Admin
# ==================================================

admin = Admin(app, name=u"管理画面", template_mode="bootstrap3")
admin.add_view(ModelView(Keystroke, db.session, name=u"キーストローク"))
admin.add_view(ModelView(User, db.session, name=u"ユーザ"))
# admin.add_view(MyKeystrokeView(Keystroke, db.session, name=u"キーストローク"))
