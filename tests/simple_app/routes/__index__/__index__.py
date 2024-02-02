from flash_flask import route

@route()
def endpoint():
    return "<h1>This is the root path</h1><a href='/hello'>Go to /hello</a>"