from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Ian!"


@app.route("/api/echo", methods=["POST"])
def echo():
    try:
        data = request.get_json()
        message = data.get("message", "")
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/add/<int:a>/<int:b>")
def add(a, b):
    result = a + b
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
