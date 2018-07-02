# -*- coding: utf-8 -*-

# ==================================================
#  Initialize Database
# ==================================================

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


# ==================================================
#  Import Models
# ==================================================

from models.keystroke import Keystroke
from models.user      import User
from models.sentence  import Sentence
