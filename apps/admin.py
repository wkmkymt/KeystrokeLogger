# -*- coding: utf-8 -*-

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app
from models import db, Keystroke, User, Sentence


# ==================================================
#  Keystroke Views
# ==================================================

class MyKeystrokeView(ModelView):
    column_list = ("id", "user_id", "sentence_id", "count", "character", "press_time", "release_time")

class MyUserView(ModelView):
    column_list = ("id", "email", "fname_k", "lname_k", "fname_r", "lname_r")

class MySentenceView(ModelView):
    column_list = ("id", "text_k", "text_r")


# ==================================================
#  Initialize Admin
# ==================================================

admin = Admin(app, name=u"管理画面", template_mode="bootstrap3", url="/admin-ks")
admin.add_view(MyKeystrokeView(Keystroke, db.session, name=u"キーストローク"))
admin.add_view(MyUserView(User, db.session, name=u"ユーザ"))
admin.add_view(MySentenceView(Sentence, db.session, name=u"文章"))
