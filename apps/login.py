# -*- coding: utf-8 -*-

import os
import json

from flask       import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required, current_user, login_user, logout_user

from models import User
from config import GOOGLE


# ==================================================
#  Initialize
# ==================================================

app = Blueprint("login", __name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


# ==================================================
#  Routing
# ==================================================

@app.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    google = GOOGLE.get_google_auth()
    auth_url, state = google.authorization_url(GOOGLE.AUTH_URL, access_type = "offline")
    session["oauth_state"] = state
    return redirect(auth_url)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@app.route("/login/authorized")
def authorized():
    if current_user and current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if "code" not in request.args and "state" not in request.args:
        return redirect(url_for(".login"))

    google = GOOGLE.get_google_auth(state = session["oauth_state"])
    try:
        token = google.fetch_token(GOOGLE.TOKEN_URL, client_secret = GOOGLE.CLIENT_SECRET, authorization_response = request.url)
    except:
        return redirect(url_for("main.index"))

    google = GOOGLE.get_google_auth(token = token)
    resp   = google.get(GOOGLE.USER_INFO)
    if resp.status_code == 200:
        user_data = resp.json()
        user = User.query.filter_by(email = user_data["email"]).first()
        if user is None:
            user = User(json.dumps(token), user_data["email"], user_data["family_name"], user_data["given_name"])
            User.save(user)
        login_user(user)
    return redirect(url_for("main.index"))
