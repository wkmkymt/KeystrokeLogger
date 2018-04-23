# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect

from models import db, User, Keystroke


# ==================================================
#  Initialize
# ==================================================

app = Blueprint("main", __name__)


# ==================================================
#  Routing
# ==================================================

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    # Get Method
    if request.method == "GET":
        return render_template("signup.html")

    # Post Method
    user = User(
        request.form["first_name"]
    )
    db.session.add(user)
    db.session.commit()

    return redirect("/")


@app.route("/register/", methods=["GET"])
@app.route("/register/<user_id>", methods=["GET"])
@app.route("/auth/", methods=["GET"])
@app.route("/auth/<user_id>", methods=["GET"])
def keystroke(user_id=None):
    # None ID
    if not user_id:
        return redirect("/")

    # Keystroke Experiment
    return render_template("keystroke.html")
