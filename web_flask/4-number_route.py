#!/usr/bin/python3
""" scripts that start a web apllication"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    "Returns some text"
    return 'HELLO HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "Returns other text"
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_test(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
