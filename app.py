from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello():
    return "hello world"

if __name__=="_main_":
    app.run(debug=True)