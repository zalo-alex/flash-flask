import os
import importlib.machinery

class Mapper:
    
    def get_route_split_path(path):
        return path.replace("\\", "/").replace("[", "<").replace("]", ">").split("/")[1:-1]

    def __init__(self, app, path) -> None:
        self.app = app
        self.path = path
        self.routes = []

    def init_routes(self):
        self.list_dir(self.path)

    def add_route(self, path):
        loader = importlib.machinery.SourceFileLoader('route', path)
        route = loader.load_module()

        split_path = Mapper.get_route_split_path(path)
        
        if split_path[-1] == "__index__":
            split_path = split_path[:-1]

        try:
            self.app.extra_files.append(path)
            route_path = '/' + '/'.join(split_path)
            self.routes.append(route_path)
            self.app.flask.add_url_rule(route_path, "_".join(split_path), route.endpoint, **route.endpoint.options)
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