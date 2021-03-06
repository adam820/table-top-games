"""
Bottle WSGI webapp
"""

from bottle import abort
from bottle import request
from bottle import static_file
from bottle import template
from bottle import Bottle

from ttg.net import new_connection_established


app = Bottle()


@app.get('/')
def index():
    return template('index')


@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    new_connection_established(wsock)
