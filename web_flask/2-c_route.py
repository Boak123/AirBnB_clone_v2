#!/usr/bin/python3
""" that starts a Flask web application C is fun"""

from flask import Flask
app.url_map.strict_slashes = False

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
     """ Prints a Message when / is called """
    return 'HELLO HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
     """ Prints a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/text/>', strict_slashes=False)
def c_is_fun(text):
     """ Prints a Message when /c is called """
    return 'C ' + text.replace('_', ' ')

if __name == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
