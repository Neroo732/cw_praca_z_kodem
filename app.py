"""
Opi

Ten moduł zawiera funkcje do ...
"""

from flask import Flask

app = Flask(__name__)


"""
    Dodaje dwie liczby.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Suma dwóch
 """      
        
@app.route('/')
def index():
    return '<h1>Hello WSB! Greetings from Flask!</h1>'
"""
    Dodaje dwie liczby.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Suma dwóch
"""
if __name__ == "__main__":
    app.run(debug=True)
