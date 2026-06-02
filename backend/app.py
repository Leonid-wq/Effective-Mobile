import http.server
import socketserver

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_error(404, "Not Found")

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Python HTTP server running on port {PORT}")
    httpd.serve_forever()

