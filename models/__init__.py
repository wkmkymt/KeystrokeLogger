# -*- coding: utf-8 -*-

# ==================================================
#  Initialize Database
# ==================================================

from flask_sqlalchemy import SQLAlchemy
from index import app

db = SQLAlchemy(app)


# ==================================================
#  Import Models
# ==================================================

from models.keystroke import Keystroke
