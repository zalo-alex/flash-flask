def route(methods = ["GET"], options = {}):
    
    def decorator(function):
        
        def new_function(*args, **kwargs):
            return function(*args, **kwargs)
        
        new_function.options = {
            "methods": methods
        }
        new_function.options.update(options)
        
        return new_function
    
    return decorator