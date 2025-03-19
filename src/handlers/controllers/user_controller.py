from flask import request, jsonify, make_response
from services.user_service import UserService
from middlewares.authentication import auth_required
from startup.loggings import logger


class userController:
    def register(self):
      try:
          data = request.get_json()
          if not data:
              raise ValueError ("Empty payload")
          if not data.get("email") or not data.get("password"):
              raise ValueError ("payload missing password or email")
          user = UserService.register_user(data)
          logger.info(f"User registered {user["email"]}")
          return jsonify (user), 201
      
      except ValueError as e:
          logger.error(f'Registration failed: {e}')
          return jsonify({"error": str(e)}), 400
      
      except Exception as e:
          logger.error(f"Unexpected error during registration: {e}")
          return jsonify({"error": "Registration failed"}), 500
      
    def login(self):
        try:
            data = request.get_json()
            if not data:
                raise ValueError ("No input data provided")
            if not data.get("email") or not data.get("password"):
                raise ValueError ("Email and password required")
            token = UserService.login_user(data)
            response = make_response(jsonify({"message": "login successful"}))
            response.set_cookie("token", token, httponly=True, secure=True)
            logger.info(f'user logged in : {data["email"]}')
            return response
        except ValueError as e:
            logger.error(f"Login failed: {e}")
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            logger.error(f"Unexpected error occured during loggin: {e}")
            return jsonify({"error: login failed"}), 500
        
    @auth_required
    def get_profile(self):
        try:
            user_id = request.user_id
            user = UserService.get_user_profile(user_id)
            return jsonify(user)
        except Exception as e:
            logger.error(f"failed to fetch profile: {e}")
            return jsonify({"error": "Failed to fetch profile"}), 500
            
             
        