from flask import Flask, render_template, request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/send', methods=['POST'])
def publish_hello():
    sse.publish({"sender": request.data["sender"],
                "message": request.data['message']}, type='message')
    return "Message sent!"