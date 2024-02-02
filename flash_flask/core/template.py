import inspect
import os

from flash_flask import Mapper

from flask import render_template_string, url_for

def send_template(**kwargs):
    path = inspect.getouterframes(inspect.currentframe(), 1)[1].filename
    
    route_path = "/".join(Mapper.get_route_split_path(path)) + "/"
    
    base_filename = os.path.basename(path)[:-3]
    
    template = base_filename + ".html"
    style = route_path + base_filename + ".css"
    script = route_path + base_filename + ".js"
    
    folder = os.path.dirname(os.path.abspath(path))
    
    if not os.path.exists(os.path.join(folder,  style)) and base_filename == "__index__":
        style = route_path + base_filename.replace("__", "") + ".css"
    
    return render_template_string(open(os.path.join(folder, template), encoding="utf8").read(), script_src=url_for("rstatic", filename=script), style_src=url_for("rstatic", filename=style), **kwargs)