import re
import urllib
import itertools
from urlparse import urljoin

import breadpy.settings

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
    """ Maps the urls set to dict to the app route

        :param app: the bottle app
        :param urls: the urls set (route_id, path, funcname)

        :rtype: Returns a dict mapping the uid to the mapping declaration
    """
    url_map = { }
    for u in urls:
        (uid, path, funcname) = itertools.islice(u, 0, 3)
        if uid in url_map:
            raise ValuError, "Url uid=%s is not unique for given route: %s, %s" % (uid, path, funcname)
        try:
            func = import_func(funcname)
        except ImportError:
            raise ValueError, "Unable to import function %s" % funcname
        # decorate with the appropriate route
        app.route(path)(func)
        url_map[uid] = u
    return url_map


def url_resolver(url_map):
    def func(uid, *args):
        if uid in url_map:
            u = url_map[uid]
            (id, tmppath) = itertools.islice(u, 0, 2)
            path = tmppath
            # substitute keyword arguments
            for v in args:
                pattern = r':\w+'
                path = re.sub(pattern, urllib.quote(v), path)
            url = urljoin(breadpy.settings.BASE_URL, path)
            return url
        else:
            raise ValueError, "Unable to resolve url uid %s" % uid
    return func

