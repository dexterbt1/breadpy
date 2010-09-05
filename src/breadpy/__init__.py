import breadpy.settings
import yaml

def load_settings(filename, conf):
    c = yaml.load(file(filename))
    for k in c.keys():
        setattr(conf, k, c[k])

load_settings("settings.yml", breadpy.settings)

from bottle import Bottle
import breadpy.routing
import breadpy.urls
from breadpy.templates import env as template_env

app = Bottle()

url_map = breadpy.routing.map_urls(app, breadpy.urls.urls)

template_env.globals['url'] = breadpy.routing.url_resolver(url_map)
