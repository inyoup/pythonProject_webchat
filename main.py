from flask import *
from flask_socketio import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('div click event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('div click response', json, callback=messageReceived)

@socketio.on('div blur event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('div blur response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)