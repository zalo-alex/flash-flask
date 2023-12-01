import os
import importlib.machinery

class Mapper:

    def __init__(self, app, path) -> None:
        self.app = app
        self.path = path

    def init_routes(self):
        self.list_dir(self.path)

    def add_route(self, path):
        loader = importlib.machinery.SourceFileLoader('route', path)
        route = loader.load_module()

        url_path = path[:-3].replace("\\", "/").replace("[", "<").replace("]", ">").split("/")[1:]
        
        if url_path[-1] == "__index__":
            url_path = url_path[:-1]

        try:
            route_path = '/' + '/'.join(url_path)
            self.app.flask.add_url_rule(route_path, "_".join(url_path), route.endpoint, **route.endpoint.options)
            print(f" + NEW ROUTE: {route_path} ({route.endpoint.options})")
        except Exception as e:
            print(e)

    def is_route(self, filename):
        return filename.split(".")[-1] == "py"

    def list_dir(self, path):
        files = os.listdir(path)
        
        for file in files:
            file_path = os.path.join(path, file)

            if os.path.isdir(file_path):
                self.list_dir(file_path)
            else:
                if self.is_route(file):
                    self.add_route(file_path)