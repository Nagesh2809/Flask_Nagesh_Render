from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my API!"

@app.route("/predict", methods=["GET"])
def predict():
    data = request.args.get("input", "default")
    response = {
        "input": data,
        "prediction": "This is a dummy prediction"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
