from flask import Flask

from flash_flask.core.routes.Mapper import Mapper

class App:

    def __init__(self, import_name, verbose = False, routes_folder = "routes", *args, **kwargs) -> None:
        self.flask = Flask(import_name, *args, **kwargs)
        self.verbose = verbose
        self.routes_folder = routes_folder

    def map_routes(self):
        mapper = Mapper(self, self.routes_folder)
        mapper.init_routes()

    def run(self, *args, **kwargs):
        self.map_routes()

        self.flask.run(*args, **kwargs)
