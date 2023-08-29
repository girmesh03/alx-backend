#!/usr/bin/env python3
"""
1-app Module

This module contains the Flask app setup with Babel configuration.
"""

from flask import Flask, render_template
from flask_babel import Babel

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


@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
