from flask import Flask
import random

app = Flask(__name__)

SECRET_NUMBER = random.randint(0, 9)


@app.route("/")
def home():
    return """
    <h1 style='color: purple;'>Guess a number between 0 and 9</h1>
    <h2>Type your guess in the URL.</h2>
    <p>Example: http://127.0.0.1:5000/5</p>
    <img src="https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif" width="300">
    """


@app.route("/<int:guess>")
def guess_number(guess):

    if guess < SECRET_NUMBER:
        return f"""
        <h1 style='color:red;'>📉 Too Low! Try Again.</h1>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="300">
        """

    elif guess > SECRET_NUMBER:
        return f"""
        <h1 style='color:blue;'>📈 Too High! Try Again.</h1>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="300">
        """

    else:
        return f"""
        <h1 style='color:green;'>🎉 You Found Me!</h1>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="300">
        """


if __name__ == "__main__":
    app.run(debug=True)