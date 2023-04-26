#!/usr/bin/env python3
"""Force locale with a URL parameter"""

from flask import Flask, request, g, render_template
from flask_babel import Babel, get_locale


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config():
    """class configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """if locale is in the request, return it"""
    if g.get('current locale'):
        return g.current_locale

    locale = request.args.get('locale')
    if locale and locale in 'LANGUAGES':
        g.current_locale = locale
        return locale
    return request.accept_languages.best_match(['LANGUAGES'])


@app.route("/")
def index_page():
    """render the template"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
