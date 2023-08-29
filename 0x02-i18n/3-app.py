#!/usr/bin/env python3
"""module for 3-app.py"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def hello() -> str:
    """Render the 3-index.html template."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
