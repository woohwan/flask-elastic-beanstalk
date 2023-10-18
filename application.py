from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    """ return a friendly HTTP greeting. """
    print("I am inside hello world")
    return "Continuous Delivery Demo"
  
@app.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name }
    return jsonify(val)
  
  
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying product app.
    app.debug = True
    app.run()

