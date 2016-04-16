from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"

@app.route("/echo/<id>")
def echo(id):
    if id > 5:
        return "Five"
    else:
        return id

if __name__ == "__main__":
    app.run()