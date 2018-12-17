# -*- coding: utf-8 -*-

from datetime import datetime

from flask       import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models         import User, Sentence, Keystroke
from .login_manager import login_manager


# ==================================================
#  Initialize
# ==================================================

app = Blueprint("main", __name__)


# ==================================================
#  Routing
# ==================================================

@app.route("/")
def index():
    if current_user.is_authenticated:
        keystrokes = Keystroke.getKeystrokesByUser(current_user.id)
    else:
        keystrokes = None
    return render_template("index.html", keystrokes = keystrokes)


@app.route("/preset", methods=["GET", "POST"])
@login_required
def preset():
    if request.method == "GET":
        if Keystroke.getKeystrokesByUser(current_user.id):
            return redirect(url_for(".index"))
        return render_template("preset.html")
    else:
        user = current_user
        user.lname_r = request.form["last_name"]
        user.fname_r = request.form["first_name"]
        User.save(user)
        return redirect(url_for(".register"))


@app.route("/register", methods=["GET", "POST"])
@login_required
def register():
    if request.method == "GET":
        if current_user.lname_r == None or current_user.fname_r == None:
            return redirect(url_for(".preset"))
        if Keystroke.getKeystrokesByUser(current_user.id):
            return redirect(url_for(".index"))
        sentence = Sentence.getLast()
        return render_template("register.html", sentence = sentence)
    else:
        strokesList = request.json["strokesList"]
        for index, strokes in enumerate(strokesList):
            for stroke in strokes:
                Keystroke.save(current_user.id, current_user.id, index, stroke["key"], stroke["press"], stroke["release"])
        return "OK!"


@app.route("/authtest")
@login_required
def authtest():
    return render_template("authtest.html")
