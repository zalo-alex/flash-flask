> [!WARNING]  
> This module is no longer maintained !

# Flash Flask
> A more organized way of using flask

## Getting started

### First App
App is like Flask, to access direct Flask app you just have to use `app.flask`
```python
from flash_flask import App

app = App(__name__)

if __name__ == "__main__":
    app.run(debug=True)
```

### Routing
In a folder named `routes` make a first folder named `__index__` with a `__index__.py` in it
```
routes
└ __index__
  └ __index__.py
main.py
```
> Route for `/`
> 
Then make it a route by editing `__index__.py` like that:
```python
from flash_flask import route

@route()
def endpoint():
	return "Hello World from Flash Flask !"
```
`__index__` indicates the path base, `@route()` indicates a route, all route functions must be called `endpoint`.

### More routes
```
routes
└ users
  └ list
    └ list.py
main.py
```
> Route for `/users/list`

### Use params in routes

```
routes
└ data
  └ [id]
    └ [id].py
main.py
```

> Route for `/data/<id>`

Here, the `[id]` replace the `<id>` of Flask, and you still can use it as param in the endpoint function

### Methods in Routes
Like flask, you just have to add `methods=[]` like that:
```python
from flash_flask import route

@route(methods=["POST", "DELETE"])
def endpoint():
	return "Hello World from Flash Flask !"
```
### Templates
Like routing, you need to create a file in the path folder:
```
routes
└ __index__
  ├ __index__.html
  └ __index__.py
main.py
```
just use `send_template` like `render_template` to send the template
```python
from flash_flask import route, send_template

@route()
def endpoint():
	return send_template()
```

### Get a site map

By using `app.set_site_map("/sitemap")` you will be able to have a sitemap of all routes
