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
        crearCount = Keystroke.getCreatCount(current_user.id)
    else:
        crearCount = 1
    return render_template("index.html", crearCount = crearCount)


@app.route("/preset", methods=["GET", "POST"])
@login_required
def preset():
    if request.method == "GET":
        return render_template("preset.html")
    else:
        user = current_user
        user.lname_r = request.form["last_name"]
        user.fname_r = request.form["first_name"]
        User.save(user)
        return redirect(url_for(".index"))


@app.route("/register", methods=["GET", "POST"])
@login_required
def register():
    if request.method == "GET":
        if current_user.lname_r == None or current_user.fname_r == None:
            return redirect(url_for(".preset"))
        clearCount = Keystroke.getCreatCount(current_user.id)
        if clearCount >= 5:
            return redirect(url_for(".index"))
        sentence = Sentence.getByID(clearCount + 1)
        if sentence.id == 4:
            sentence.text_k = sentence.text_k.replace("[LAST]", current_user.lname_k)
            sentence.text_r = sentence.text_r.replace("[LAST]", current_user.lname_r)
            sentence.text_k = sentence.text_k.replace("[FIRST]", current_user.fname_k)
            sentence.text_r = sentence.text_r.replace("[FIRST]", current_user.fname_r)
        return render_template("register.html", sentence = sentence)
    else:
        clearCount  = Keystroke.getCreatCount(current_user.id)
        strokesList = request.json["strokesList"]
        for index, strokes in enumerate(strokesList):
            for stroke in strokes:
                Keystroke.save(current_user.id, clearCount + 1, index, stroke["key"], stroke["press"], stroke["release"])
        return "OK!"


@app.route("/authtest")
@login_required
def authtest():
    return render_template("authtest.html")


@app.route("/deleteall")
@login_required
def deleteall():
    Keystroke.deleteAll()
    return redirect(url_for(".index"))