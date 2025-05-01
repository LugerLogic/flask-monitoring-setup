from flask import Flask
from prometheus_client import start_http_server, Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')


@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route('/')
def home():
    REQUEST_COUNT.inc()  
    return "Hello there!"

if __name__ == '__main__':
    start_http_server(8000)  
    app.run(host='0.0.0.0', port=5000)