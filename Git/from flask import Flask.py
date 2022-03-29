from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)
@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/editor_intro')
def editor_intro():
   return render_template('editor_intro.html')

#接受消息的回调函数
@socketio.on('send_content')
def get_editor_content(message):
   print('message')
   print(message['contents'])
   
   #  socketio.emit('init_trade_success',{'types':types})


if __name__ == '__main__':
   app.run()