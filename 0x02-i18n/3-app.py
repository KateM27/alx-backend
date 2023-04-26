#!/usr/bin/env python3
"""parametrize templates"""

from flask import Flask, request, g, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """class configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """if user is logged in, use locale from the default user settings"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route("/")
def index_page():
    """render the parametrized template"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
