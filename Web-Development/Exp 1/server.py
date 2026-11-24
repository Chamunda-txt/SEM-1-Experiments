
from http.server import HTTPServer, SimpleHTTPRequestHandler

host = "127.0.0.1"
port = 8000

server = HTTPServer((host, port), SimpleHTTPRequestHandler)

print(f"Server running at http://{host}:{port}")

server.serve_forever()
