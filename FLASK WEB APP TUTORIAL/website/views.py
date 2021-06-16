from flask import Blueprint, render_template
# Blueprint : it has bunch of roots inside, URLs defined in.
# 這裡import Blueprint 的用意為與app區隔開來，不用侷限在單獨檔案

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
