from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"


@app.route("/about")
def about():
    return """
    <h2>About Me</h2>
    <p>I am learning Flask in the 100 Days of Python Bootcamp.</p>
    """


@app.route("/contact")
def contact():
    return """
    <h2>Contact</h2>
    <p>Email: example@gmail.com</p>
    """


if __name__ == "__main__":
    app.run(debug=True)