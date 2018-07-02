# -*- coding: utf-8 -*-

# ==================================================
#  Initialize Flask
# ==================================================

from flask import Flask
from config import BaseConfig

app = Flask(__name__, static_folder="./statics")
app.config.from_object(BaseConfig)

# ==================================================
#  Application
# ==================================================

from apps import login
from apps import main
from apps import admin

app.register_blueprint(login.app, url_prefix="/user")
app.register_blueprint(main.app,  url_prefix="")
