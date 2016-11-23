'''
Refs:
  https://gist.github.com/bradmontgomery/2219997
'''
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer as Server
import os


class Handler(BaseHTTPRequestHandler):
  '''Handles incoming http requests.'''
  def send_200(self):
    self.send_response(200)
    # self.send_header('Content-type', 'text/html')
    self.end_headers()

  def send_404(self):
    self.send_error(404)
    self.end_headers()

  def do_GET(self):
    targets = ('', '/index.html', '/index.htm')
    path = './pub/' + self.path

    for p in (os.path.abspath(path + s) for s in targets):
      try:
        with open(p, 'r') as f:
          self.send_200()
          self.wfile.writelines(f)
          return
      except IOError:
        pass

    self.send_404()


def run(port=8000):
  '''
  Starts the local web server.

  Args:
    port (int): The port for the server to listen on.
  '''
  address = ('', port)
  httpd = Server(address, Handler)
  print('HTTP server starting...')
  httpd.serve_forever()


if __name__ == '__main__':
  run()
