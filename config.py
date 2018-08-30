# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth2Session


# ==================================================
#  Basic Config
# ==================================================

class BaseConfig(object):
    DEBUG                          = True
    SECRET_KEY                     = "gq7j847gq7j847gq7j847"
    DATABASE_FILE                  = "dbs/keystroke.db"
    SQLALCHEMY_DATABASE_URI        = "sqlite:////" + DATABASE_FILE
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    OAUTH1_PROVIDER_ENFORCE_SSL    = False


# ==================================================
#  OAuth2 for Google Config
# ==================================================

class GOOGLE(object):
    CLIENT_ID     = "767804331266-s5tn2psi484k2c5n5d2e7sl9blef7pqi.apps.googleusercontent.com"
    CLIENT_SECRET = "hItrQiau-ss9QDmx_3vua1UU"
    REDIRECT_URI  = "https://keystroke-logger.herokuapp.com/user/login/authorized"
    # REDIRECT_URI  = "http://localhost:5000/user/login/authorized"

    AUTH_URL  = "https://accounts.google.com/o/oauth2/auth"
    TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
    USER_INFO = "https://www.googleapis.com/userinfo/v2/me"
    SCOPE     = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]

    @classmethod
    def get_google_auth(cls, state = None, token = None):
        if token:
            return OAuth2Session(cls.CLIENT_ID, token = token)
        if state:
            return OAuth2Session(cls.CLIENT_ID, state = state, redirect_uri = cls.REDIRECT_URI, scope = cls.SCOPE)
        return OAuth2Session(cls.CLIENT_ID, redirect_uri = cls.REDIRECT_URI, scope = cls.SCOPE)
