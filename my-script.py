from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Python Flask!"

if __name__ == "__main__":
    # Change port here (e.g., 8000)
    app.run(host="127.0.0.0", port=8000)
