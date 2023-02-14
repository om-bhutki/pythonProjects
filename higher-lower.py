from flask import Flask
import random

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9!</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200>"


number = random.randint(0, 9)


@app.route("/<int:guessed_number>")
def guess(guessed_number):
    if guessed_number < number:
        return "<h1 style='color: red'>Too low try again!</h1>" \
               '<img src="https://media.giphy.com/media/q4ICE9wYvOwBG/giphy.gif`" width=200> '
    elif guessed_number == number:
        return "<h1 style='color: green'>You got it!</h1>" \
               '<img src="https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif" width=200> '

    else:
        return "<h1 style='color: red'>Too high try again!</h1>" \
                '<img src="https://media.giphy.com/media/69yrZWuu7clVYvmtJi/giphy.gif" width=200> '


if __name__ == "__main__":
    app.run(port=4999, debug=True)
