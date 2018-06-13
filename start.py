from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
        return "Hello World"
@myapp.route("/tiide")
def tiide():
            return "Welcome to TIIDE World"
if __name__=="__main__":    
    app.run()
