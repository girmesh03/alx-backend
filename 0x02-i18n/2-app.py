#!/usr/bin/env python3
"""
2-app Module

This module contains the Flask app setup with Babel configuration and get_locale function.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class with language configuration.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages based on request.accept_languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
