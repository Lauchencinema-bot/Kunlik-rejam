from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

os.chdir(Path(__file__).parent)
server = ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)
print("Ish Vaqtim serveri ishga tushdi:")
print("http://127.0.0.1:8000")
print("To'xtatish: Ctrl+C")
server.serve_forever()
