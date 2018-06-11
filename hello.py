from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/min")
def min():
    return "Min Min"

if_name_=="_main_":
    app.run()

