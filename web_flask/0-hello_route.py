#!/usr/bin/python3
"""Run a flask app that returns Hello HBNB"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":

    # start the Flask development server
    # Listen on all available network interfaces and port 5000
    app.run(host="0.0.0.0", port=5000)
