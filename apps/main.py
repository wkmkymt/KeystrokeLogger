# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect

from models import Keystroke


# ==================================================
#  Initialize
# ==================================================

app = Blueprint("main", __name__)


# ==================================================
#  Routing
# ==================================================

@app.route("/")
def index():
    return render_template("register.html")
