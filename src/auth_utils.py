import jwt
from functools import wraps
from flask import request, jsonify
from src.config import Config

def generate_token(user_id):
    """
    Generates a JWT token for a given user_id.
    """
    token = jwt.encode({"user_id": user_id}, Config.JWT_SECRET_KEY, algorithm="HS256")
    return token

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", None)
        
        if not auth_header:
            return jsonify({"message": "Missing Authorization header"}), 401
        
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return jsonify({"message": "Invalid Authorization header format"}), 401
        
        token = parts[1]
        try:
            decoded = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
            user_id = decoded.get("user_id")
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401
        
        return func(user_id, *args, **kwargs)
    return decorated
