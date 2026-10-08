from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

os.chdir(Path(__file__).parent)

port = int(os.environ.get("PORT", 8000))

server = ThreadingHTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)

print("Kunlik-rejam serveri ishga tushdi")
print(f"Port: {port}")

server.serve_forever()