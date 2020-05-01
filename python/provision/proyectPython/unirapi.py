from flask import Flask
api = Flask(__name__)

@api.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    api.run(host='0.0.0.0')
