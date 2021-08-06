from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, rooms
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return "hello_world"

#this is the route which will be used by the restaurant
@app.route('/restaurant/<id>')
def restaurant_home(id):
    return render_template("index.html")

#this route will be used by the devices
@app.route('/device/<id>')
def device_home(id):
    return render_template("devices.html")

#client joins the server through the mobile device
#This function gets a uid for the restaurant using which the client joins the server
@socketio.on('message',namespace="/restaurant")
def client(uid):
	join_room(uid)

#devices will join the server through this route
#This function gets a uid for the restaurant using which the device joins the server
@socketio.on('message',namespace="/device")
def device(uid):
	join_room(uid)
	emit("test",uid,namespace="/restaurant",room=uid)


if __name__ == '__main__':
    socketio.run(app, debug=True,host="0.0.0.0")
