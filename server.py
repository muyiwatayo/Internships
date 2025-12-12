from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
import os

USERS_FILE = "users.json"

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

class SimpleHandler(BaseHTTPRequestHandler):
    sessions = {}

    def _set_headers(self, status=200, content_type="text/html"):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        path = self.path
        if path == "/":
            self._serve_file("index.html")
        elif path == "/signup":
            self._serve_file("signup.html")
        elif path == "/login":
            self._serve_file("login.html")
        elif path == "/welcome":
            cookies = self.headers.get('Cookie')
            username = None
            if cookies:
                for cookie in cookies.split(';'):
                    k,v = cookie.strip().split('=')
                    if k == "session" and v in self.sessions:
                        username = self.sessions[v]
            if username:
                self._serve_file("welcome.html", username=username)
            else:
                self._redirect("/login")
        elif path.startswith("/static/"):
            self._serve_file(path[1:], "text/css")
        else:
            self._set_headers(404)
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(length).decode()
        data = urllib.parse.parse_qs(post_data)

        if self.path == "/signup":
            username = data.get("username", [""])[0]
            password = data.get("password", [""])[0]
            users = load_users()
            if username in users:
                self._set_headers()
                self.wfile.write(b"Username already exists.")
            else:
                users[username] = {"password": password}
                save_users(users)
                self._set_headers()
                self.wfile.write(b"Signup successful! <a href='/login'>Login here</a>")

        elif self.path == "/login":
            username = data.get("username", [""])[0]
            password = data.get("password", [""])[0]
            users = load_users()
            if username in users and users[username]["password"] == password:
                import uuid
                token = str(uuid.uuid4())
                self.sessions[token] = username
                self.send_response(302)
                self.send_header("Location", "/welcome")
                self.send_header("Set-Cookie", f"session={token}")
                self.end_headers()
            else:
                self._set_headers()
                self.wfile.write(b"Invalid credentials. <a href='/login'>Try again</a>")
        else:
            self._set_headers(404)
            self.wfile.write(b"404 Not Found")

    def _serve_file(self, filename, username=None, content_type="text/html"):
        try:
            with open(filename, "rb") as f:
                content = f.read()
            self._set_headers(content_type=content_type)
            if username and filename == "welcome.html":
                content = content.replace(b"{{username}}", username.encode())
            self.wfile.write(content)
        except FileNotFoundError:
            self._set_headers(404)
            self.wfile.write(b"404 Not Found")

    def _redirect(self, url):
        self.send_response(302)
        self.send_header("Location", url)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    print(f"Starting server at http://127.0.0.1:{port}")
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
