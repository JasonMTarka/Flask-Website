from flask import Flask
from portfolio_site.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from portfolio_site.coronavirus.routes import covid
    from portfolio_site.sudoku.routes import sudoku
    from portfolio_site.pass_gen.routes import pass_gen
    from portfolio_site.main.routes import main
    from portfolio_site.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(covid)
    app.register_blueprint(sudoku)
    app.register_blueprint(pass_gen)
    app.register_blueprint(errors)

    return app
