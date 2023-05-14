"""
Opi

Ten moduł zawiera funkcje do ...
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Add two numbers"""
    return '<h1>Hello WSB! Greetings from Flask!</h1>'


"""
Opi

:return: ddddd
"""

if __name__ == "__main__":
    app.run(debug=True)
