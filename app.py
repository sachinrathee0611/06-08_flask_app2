from flask import Flask, jsonify, request

app = Flask(__name__)


def _get_number(payload, key):
    value = payload.get(key)
    if value is None:
        raise ValueError(f"Missing field: {key}")
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Field '{key}' must be a number") from exc


@app.get("/")
def home():
    return jsonify(
        message="CI Demo API is running",
        endpoints=["/", "/health", "/add", "/subtract", "/multiply", "/divide"],
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/add")
def add():
    try:
        payload = request.get_json(silent=True) or {}
        a = _get_number(payload, "a")
        b = _get_number(payload, "b")
        return jsonify(operation="add", result=a + b)
    
    except ValueError as e:
        return jsonify(error=str(e)), 400


@app.post("/subtract")
def subtract():
    payload = request.get_json(silent=True) or {}
    a = _get_number(payload, "a")
    b = _get_number(payload, "b")
    return jsonify(operation="subtract", result=a - b)


@app.post("/multiply")
def multiply():
    payload = request.get_json(silent=True) or {}
    a = _get_number(payload, "a")
    b = _get_number(payload, "b")
    return jsonify(operation="multiply", result=a * b)


@app.post("/divide")
def divide():
    payload = request.get_json(silent=True) or {}
    a = _get_number(payload, "a")
    b = _get_number(payload, "b")
    if b == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    return jsonify(operation="divide", result=a / b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
