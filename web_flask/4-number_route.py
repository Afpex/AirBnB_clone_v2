#!/usr/bin/python3
"""Run a flask app that returns Hello HBNB"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns 'HBNB'"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """Configure C is Fun"""
    text = text.replace('_', ' ')
    value = 'C {}'.format(text)
    return value


@app.route("/python/", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_is_fun(text='is cool'):
    """Configure Python is Fun"""
    text = text.replace('_', ' ')
    value = 'Python {}'.format(text)
    return value


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Check and return if it is an integer"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
