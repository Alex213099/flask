from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello():
    return"Hello This is Nganga Faith"

if __name__=="__main__":
    app.run(debug=True)