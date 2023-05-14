"""
Opi

Ten moduł zawiera funkcje do ...
"""

from flask import Flask

app = Flask(__name__)
"""
Opi

Ten moduł zawiera funkcje do ...
"""


@app.route('/')
def index():
    return '<h1>Hello WSB! Greetings from Flask!</h1>'
"""
Opi

:return: ddddd
"""

if __name__ == "__main__":
    app.run(debug=True)
