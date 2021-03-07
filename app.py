import requests
import os
from flask import Flask, send_from_directory, json, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
from APICalls import fetchlast24hours

app = Flask(__name__, static_folder='./build/static')

cors = CORS(app, resources={r"/*": {"origins": "*"}})

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    json=json,
    manage_session=False,
    # engineio_logger=True used for debugging purposes
)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # reloads the cache every time 

@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)
    

@socketio.on('connect')
def on_connect():
    """Test"""
    print('User Connected!')


@socketio.on('disconnect')
def on_disconnect():
    """Test"""
    print('User Disconnected!')

@socketio.on('search')
def on_search(data):
    """Test"""
    datelst, openlst, closelst, highlst, lowlst, volumelst, symbol = fetchlast24hours(data['stock'])
    socketio.emit('StockCall', {'datelst': datelst, 'openlst':  openlst,
                  'closelst': closelst, 'highlst': highlst, 'lowlst': lowlst, 'volumelst': volumelst, 'symbol': symbol}, broadcast=True,
                  include_self=True)


if __name__ == "__main__":
# Note that we don't call app.run anymore. We call socketio.run with app arg
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
