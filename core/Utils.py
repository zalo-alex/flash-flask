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
    
    def get_optional_json_values(array: list):
        values = [value for value in map(lambda key: request.json.get(key), array)]
        not_none = []
        [not_none.append(value) if value != None else None for value in values]                
        
        if not not_none:
            raise Exception("Invalid request data")

        return not_none