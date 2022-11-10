from flask import Flask, jsonify

app = Flask(__name__)


# Endpoint

@app.get("/")
# Homepage
def index():
    return "hello"

@app.get("/hello")
def say_hello():
    return jsonify({"message":"sup"})


if __name__ == "__main__":
  app.run(debug=True)