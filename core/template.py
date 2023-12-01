import inspect
import os

from flask import render_template_string

def send_template(**kwargs):
    path = inspect.getouterframes(inspect.currentframe(), 1)[1].filename
    filename = os.path.basename(path)[:-3] + ".html"
    folder = os.path.dirname(os.path.abspath(path))
    
    return render_template_string(open(os.path.join(folder, filename), encoding="utf8").read(), **kwargs)