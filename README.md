```markdown
# Caching Proxy Server

This project is a Django-based CLI tool that starts a caching proxy server, forwarding requests to an origin server and caching the responses for future use.

## Usage

### Start the Proxy Server
Run the following command to start the proxy server:
```bash
python manage.py proxy_server --port <port> --origin <origin-url>
```
Example:
```bash
python manage.py proxy_server --port 3000 --origin http://dummyjson.com
```

### Clear Cache
To clear the cache, run:
```bash
python manage.py proxy_server --clear-cache
```

## Features
- Forwards requests and caches responses.
- Adds `X-Cache: HIT` or `X-Cache: MISS` headers to responses.
- Simple command to clear the cache.

## Requirements
- Python 3.8+
- Django
- requests
- cachetools

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/caching-proxy.git
    cd caching-proxy
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the proxy server as described above.

## Project Roadmap

For the detailed roadmap of how this project works and can be extended, please visit:  
[https://roadmap.sh/projects/caching-server](https://roadmap.sh/projects/caching-server)
```

This version includes the required link to the roadmap at the end.
