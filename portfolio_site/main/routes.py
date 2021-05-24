from flask import Blueprint, render_template, url_for

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home() -> str:
    image_file = url_for("static", filename="pictures/" + "profile_pic.jpg")
    return render_template("home.html", title="My Flask Website", image_file=image_file)
