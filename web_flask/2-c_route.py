#!/usr/bin/python3
"""Starts a flask webapp that returns 'Hello HBNB'"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns 'HBNB'"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """ Returns a message when /c is called """
    text = text.replace('_', ' ')
    value = 'C {}'.format(text)
    return value


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
