# -*- coding: utf-8 -*-

# ==================================================
#  Basic Config
# ==================================================

class BaseConfig(object):
    DEBUG                          = True
    SECRET_KEY                     = "gq7j847gq7j847gq7j847"
    DATABASE_FILE                  = "dbs/keystroke.db"
    SQLALCHEMY_DATABASE_URI        = "sqlite:///" + DATABASE_FILE
    SQLALCHEMY_TRACK_MODIFICATIONS = True
