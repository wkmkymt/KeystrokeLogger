# -*- coding: utf-8 -*-

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app
from models import db, Keystroke, User, Sentence


# ==================================================
#  Keystroke Views
# ==================================================

class MyKeystrokeView(ModelView):
    column_list = ("user_id", "target_id", "count", "character", "press_time", "release_time")


# ==================================================
#  Initialize Admin
# ==================================================

admin = Admin(app, name=u"管理画面", template_mode="bootstrap3", url="/admin-ks")
admin.add_view(MyKeystrokeView(Keystroke, db.session, name=u"キーストローク"))
admin.add_view(ModelView(User, db.session, name=u"ユーザ"))
admin.add_view(ModelView(Sentence, db.session, name=u"文章"))
