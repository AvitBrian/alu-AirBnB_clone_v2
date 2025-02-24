#!/usr/bin/python3
"""
    a script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Displays  HBNB! """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
