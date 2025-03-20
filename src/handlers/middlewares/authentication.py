from functools import wraps
from flask import request, jsonify
from src.services_layer.auth.auth import AuthService

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token and token.startswith("Bearer "):
            token = token.split(' ')[1]
        if not token or not AuthService.verify_token(token):
            return jsonify({"error": "Unauthorized "}), 401
        return f(*args, **kwargs)
    return decorated