# -*- coding: utf-8 -*-

from flask_script import Manager

from app import app
from models import db


# ==================================================
#  Initialize
# ==================================================

manager = Manager(app)


# ==================================================
#  Managiment Command
# ==================================================

@manager.command
def create_db():
    db.create_all()


# ==================================================
#  Run
# ==================================================

if __name__=="__main__":
    manager.run()
