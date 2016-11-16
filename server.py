from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer as Server


class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    # self.wfile.write('<html><body><h1>hello</h1></body></html>')
    with open('./movies.html', 'r') as f:
      self.wfile.writelines(f)

def run(port=8000):
  address = ('', port)
  httpd = Server(address, Handler)
  print('HTTP server starting...')
  httpd.serve_forever()

if __name__ == '__main__':
  run()