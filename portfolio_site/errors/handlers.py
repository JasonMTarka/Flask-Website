from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)


# Commented out type hints until AWS supports Python 3.9

@errors.app_errorhandler(404)
def error_404(error):  # -> tuple[str, int]:
    return render_template("errors/404.html"), 404  # Other render_templates have 200 built in

# There is also a @errors.errorhandler method, but is only blueprint-wide, not app-wide like we need


@errors.app_errorhandler(403)
def error_403(error):  # -> tuple[str, int]:
    return render_template("errors/403.html"), 403


@errors.app_errorhandler(500)
def error_500(error):  # -> tuple[str, int]:
    return render_template("errors/500.html"), 500
