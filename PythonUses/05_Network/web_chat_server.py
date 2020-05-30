from flask import Flask
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)  # SocketIO에 Flask 인스탄스를 넘겨준다


@app.route("/")
def index():
    return render_template("index.html")

# connect를 받으면 다음 함수를 호출해 이벤트를 보낸다.
@socketio.on("connected")
def connect_handler():
    socketio.emit("response", {"nickname": "", "message": "새로운 유저 입장"})

# chat 이벤트가 오면 다음 함수 실행
@socketio.on("chat")
def event_handler(json):
    json["nickname"] = json["nickname"].encode("latin1").decode(
        "utf-8")  # json은 latin1 형태로 넘어오는데 이를 다시 utf-8 형태로 decode 해준다
    json["message"] = json["message"].encode("latin1").decode(
        "utf-8")  # json은 latin1 형태로 넘어오는데 이를 다시 utf-8 형태로 decode 해준다

    # response를 보낸다.
    socketio.emit(
        "response", {"nickname": json["nickname"], "message": json["message"]})


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=14000, debug=True)
