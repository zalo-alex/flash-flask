from flask import request

class Utils:
    
    def get_ip():
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            return request.environ['REMOTE_ADDR']
        else:
            return request.environ['HTTP_X_FORWARDED_FOR']
        
    def get_json_values(array: list):
        values = [value for value in map(lambda key: request.json.get(key), array)]
        if any([value == None for value in values]):
            raise Exception("Invalid request data")
        return values
    
    def get_optional_json_values(array: list, min_amount = 1):
        values = {}
        for key in array:
            if (data := request.json.get(key)) != None:
                values[key] = data    
        
        if len(values) < min_amount:
            raise Exception("Invalid request data")

        return values