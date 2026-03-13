from flask import Flask

app = Flask(__name__)

# Simple route
@app.route("/")
def hello():
    return "Hello World from Python Flask!"

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
