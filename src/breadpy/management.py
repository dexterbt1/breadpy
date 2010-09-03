from optparse import OptionParser
import bottle
import breadpy

def execute_from_commandline():
    parser = OptionParser()
    parser.add_option("-b", "--bind", dest="bind", default="127.0.0.1", help="network interface host to bind")
    parser.add_option("-p", "--port", dest="port", default=8887, help="port to serve requests")
    parser.add_option("--fastcgi", dest="fastcgi", action="store_true", help="serve using FastCGI ")
    (options, args) = parser.parse_args()
    server=bottle.WSGIRefServer
    if options:
        #print "%s" % options
        if options.fastcgi:
            server=bottle.FlupFCGIServer
    bottle.run(app=breadpy.app, server=server, host=options.bind, port=options.port)
    


