#!/usr/bin/env python3
"""
Food Bowl Rush — local game server
Serves the game and stores scores in scores.json
"""
import json, os, threading, webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

SCORES_FILE = os.path.join(os.path.dirname(__file__), 'scores.json')
PORT = 8765

def load_scores():
    try:
        with open(SCORES_FILE) as f:
            return json.load(f)
    except:
        return {}

def save_scores(data):
    with open(SCORES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

class GameHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/scores':
            self._json(200, load_scores())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/scores':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            save_scores(body)
            self._json(200, {'ok': True})

    def do_DELETE(self):
        if self.path == '/api/scores':
            save_scores({})
            self._json(200, {'ok': True})

    def _json(self, code, data):
        payload = json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(payload))
        self._cors()
        self.end_headers()
        self.wfile.write(payload)

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def log_message(self, fmt, *args):
        pass  # keep terminal quiet

def main():
    httpd = HTTPServer(('localhost', PORT), GameHandler)
    url = f'http://localhost:{PORT}'
    print(f'')
    print(f'  🍽️  Food Bowl Rush is running!')
    print(f'  📂  Scores saved to: scores.json')
    print(f'  🌐  Open: {url}')
    print(f'')
    print(f'  Press Ctrl+C to stop.')
    print(f'')
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n  👋  Server stopped. Scores are saved in scores.json')

if __name__ == '__main__':
    main()
