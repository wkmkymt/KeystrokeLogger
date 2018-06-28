# -*- coding: utf-8 -*-

from flask_login import LoginManager

from app    import app
from models import User


# ==================================================
#  Initialize
# ==================================================

login_manager = LoginManager(app)
login_manager.login_view         = "main.index"
login_manager.session_protection = "strong"


# ==================================================
#  Handler
# ==================================================

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
