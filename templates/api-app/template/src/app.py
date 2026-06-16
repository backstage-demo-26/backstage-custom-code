from flask import Flask, jsonify, request
from functools import wraps
from hmac import compare_digest
import time
import socket 

from helper import config, request_nhs_token


app = Flask(__name__)

# -----------------------------
# Security Decorator
# -----------------------------
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        provided_key = request.headers.get("x-api-key")

        if not provided_key:
            return jsonify({"error": "API key missing"}), 401

        if not compare_digest(provided_key, config.api_key):
            return jsonify({"error": "Invalid API key"}), 403

        return f(*args, **kwargs)

    return decorated


# -----------------------------
# Routes
# -----------------------------
@app.route('/api/${{values.app_name}}/v1/healthz')
def health():
    return jsonify({
        "status": "up",
        "timestamp": int(time.time())
    }), 200


@app.route('/api/${{values.app_name}}/v1/info')
def info():
    return jsonify({
        "app_name": "${{values.app_name}}",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "timestamp": int(time.time())
    })



# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    
	