# proxy/management/commands/proxy_server.py

from django.core.management.base import BaseCommand
import requests
from cachetools import TTLCache
from django.conf import settings
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Cache with TTL
cache = TTLCache(maxsize=100, ttl=300)

class Command(BaseCommand):
    help = 'Starts a caching proxy server'

    def add_arguments(self, parser):
        parser.add_argument('--port', type=int, help='Port number to run the proxy server')
        parser.add_argument('--origin', type=str, help='Origin server URL')
        parser.add_argument('--clear-cache', action='store_true', help='Clear the cache')

    def handle(self, *args, **kwargs):
        port = kwargs['port']
        origin = kwargs['origin']
        if kwargs['clear_cache']:
            cache.clear()
            self.stdout.write(self.style.SUCCESS('Cache cleared successfully!'))
        else:
            run_proxy_server(port, origin)


def run_proxy_server(port, origin):
    class ProxyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            cache_key = f"{self.command}:{self.path}"
            
            if cache_key in cache:
                self.send_response(200)
                for key, value in cache[cache_key].headers.items():
                    self.send_header(key, value)
                self.send_header('X-Cache', 'HIT')
                self.end_headers()
                self.wfile.write(cache[cache_key].content)
            else:
                origin_url = urllib.parse.urljoin(origin, self.path)
                response = requests.get(origin_url)
                cache[cache_key] = response
                self.send_response(response.status_code)
                for key, value in response.headers.items():
                    self.send_header(key, value)
                self.send_header('X-Cache', 'MISS')
                self.end_headers()
                self.wfile.write(response.content)

    httpd = HTTPServer(('localhost', port), ProxyHandler)
    print(f'Serving on port {port} and forwarding to {origin}')
    httpd.serve_forever()
