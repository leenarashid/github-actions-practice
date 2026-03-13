from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask!"

if __name__ == "__main__":
    # Use 127.0.0.1 so you can open it in your browser
    # Use port 5000 (default Flask port)
    app.run(host="127.0.0.1", port=8000)
