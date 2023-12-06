import os

from flask import Flask, send_from_directory

from flash_flask.core.routes.Mapper import Mapper

class App:

    def __init__(self, import_name, verbose = False, routes_folder = "routes", extra_files = [], *args, **kwargs) -> None:
        self.flask = Flask(import_name, *args, **kwargs)
        self.verbose = verbose
        self.routes_folder = routes_folder
        self.extra_files = extra_files
        
    def set_site_map(self, path):
        self.flask.add_url_rule(path, "_site_map", lambda *_: "<br>".join([f"<a href={route.replace('<', '[').replace('>', ']')}>{route.replace('<', '[').replace('>', ']')}</a>" for route in self.mapper.routes]))

    def map_routes(self):
        self.mapper = Mapper(self, self.routes_folder)
        self.mapper.init_routes()
        
    def rstatic(self, filename):
        static_folder = 'routes'

        path = os.path.join(static_folder, filename)
        if not os.path.isfile(path):
            return "File not found", 404
        
        if any([path.endswith(ext) for ext in [".css", ".js"]]):
            return send_from_directory(static_folder, filename)
        
        return "File not found", 404

    def run(self, *args, **kwargs):
        self.map_routes()
        
        self.flask.add_url_rule("/rstatic/<path:filename>", view_func=self.rstatic)
        
        self.flask.run(extra_files=self.extra_files, *args, **kwargs)
