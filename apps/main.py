# -*- coding: utf-8 -*-

from flask       import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models         import User, Sentence
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
    return render_template("index.html")


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
        return redirect(url_for(".register"))


@app.route("/register")
@login_required
def register():
    if request.method == "GET":
        if current_user.lname_r == None or current_user.fname_r == None:
            return redirect(url_for(".preset"))
        sentence = Sentence.getLast()
        return render_template("register.html", sentence = sentence)
    else:
        pass


@app.route("/authtest")
@login_required
def authtest():
    return render_template("authtest.html")
