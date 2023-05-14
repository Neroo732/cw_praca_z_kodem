"""
Opis modułu

Ten moduł zawiera funkcje do ...
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    Handler dla strony głównej
    
    :return: Treść strony głównej
    """
    return '<h1>Hello WSB! Greetings from Flask!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
