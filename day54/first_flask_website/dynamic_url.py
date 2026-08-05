from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def greet(name):
    return f"<h1>Hello {name.title()}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/age/<int:number>")
def age(number):
    return f"You are {number} years old."