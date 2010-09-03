import breadpy.settings as settings
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader(settings.TEMPLATE_APP_NAME, settings.TEMPLATE_DIR_NAME))

def get_template(path):
    return env.get_template(path)

