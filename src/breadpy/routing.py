import breadpy.settings
import itertools
from urlparse import urljoin

def import_func(fully_qualified_name):
    components = fully_qualified_name.split(".")
    funcname = components.pop()
    modname = ".".join(components)
    m = __import__(modname)
    for comp in components[1:]: 
        m = getattr(m, comp)
    func = getattr(m, funcname)
    return func

def map_urls(app, urls):
    """Map urls to route information"""
    url_map = { }
    for u in urls:
        (uid, path, funcname) = itertools.islice(u, 0, 3)
        if uid in url_map:
            raise ValuError, "urls uid=%s is not unique for route: %s, %s" % (uid, path, funcname)
        func = import_func(funcname)
        # decorate with the appropriate route
        app.route(path)(func)
        url_map[uid] = u
    return url_map


def url_resolver(url_map):
    def func(uid):
        url = u''
        if uid in url_map:
            u = url_map[uid]
            (id, path) = itertools.islice(u, 0, 2)
            url = urljoin(breadpy.settings.BASE_URL, path)
        return url
    return func

