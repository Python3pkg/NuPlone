import os
import http.server
import http.server


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    do_POST = http.server.SimpleHTTPRequestHandler.do_GET

    def guess_type(self, path):
        if '@@' in path:
            return 'text/html'
        return http.server.SimpleHTTPRequestHandler.guess_type(self, path)


if __name__ == '__main__':
    directory = os.path.dirname(__file__)
    os.chdir(os.path.join(directory, os.pardir))
    print('You can view the prototype at http://localhost:8000/Prototype/')
    http.server.test(RequestHandler, http.server.HTTPServer)
