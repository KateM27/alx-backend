#!/usr/bin/env python3
"""Basic flask application with a single route"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """route for my simple app"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
