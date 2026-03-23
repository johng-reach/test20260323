"""Simple Hello World API using Python's built-in http.server."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/hello":
            # Return a JSON hello world response
            body = json.dumps({"message": "Hello, World!"}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(body))
            self.end_headers()
            self.wfile.write(body)
        else:
            # Return 404 for any other path
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress default access log output
        pass


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), HelloHandler)
    print("Hello World API running at http://localhost:8000/hello")
    server.serve_forever()
