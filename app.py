from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> This is the index page </h1>"


if __name__ == '__main__':
    app.config(debug=True)
