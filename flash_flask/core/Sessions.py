from functools import wraps
import secrets
import logging

from flask import request, session

class Sessions:

    __TOKENS = {}
    __DATA = {}
    __GET_USER_FUNCTION = None
    
    def set_get_user(function):
        Sessions.__GET_USER_FUNCTION = function

    def add_session(id):
        token = secrets.token_urlsafe(64)
        Sessions.__TOKENS[token] = id
        Sessions.__DATA[token] = {}
        session["token"] = token
        return token
    
    def get_user_id(token):
        for token in Sessions.__TOKENS:
            return Sessions.__TOKENS[token]
        return None
    
    def store_client_side_data(key, data):
        if hasattr(request, "token"):
            session[request.token][key] = data
        else:
            raise Exception("Use @Sessions.required() to store data")
            
    def get_client_side_data(key, default = None):
        
        if not hasattr(request, "token"):
            raise Exception("Use @Sessions.required() to get data")
        
        if key not in session[request.token]:
            return default
        
        return session[request.token][key]
    
    def store_server_side_data(key, data):
        if hasattr(request, "token"):
            Sessions.__DATA[request.token][key] = data
        else:
            raise Exception("Use @Sessions.required() to store data")
            
    def get_server_side_data(key, default = None):
        
        if not hasattr(request, "token"):
            raise Exception("Use @Sessions.required() to get data")
        
        if key not in Sessions.__DATA[request.token]:
            return default
        
        return Sessions.__DATA[request.token][key]

    def required(response = lambda *_: {"error": "You need to be logged"}):
        
        def decorator(f):
            @wraps(f)
            def new_function(*args, **kwargs):
                token = session.get("token")

                if not token or token not in Sessions.__TOKENS:
                    return response()

                user_id = Sessions.get_user_id(token)

                if not Sessions.__GET_USER_FUNCTION:
                    raise Exception("GET_USER function is not set, use Sessions.set_get_user()")
                
                user = Sessions.__GET_USER_FUNCTION(user_id)
                
                request.token = token
                
                return f(user, *args, **kwargs)
            return new_function

        return decorator