from flask import Flask, render_template, request
from flask_sse import sse
import os
app = Flask(__name__)
app.config["REDIS_URL"] = os.environ.get('REDISCLOUD_URL')
app.register_blueprint(sse, url_prefix='/stream')
app.config['DEBUG'] = True
@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/send', methods=['POST'])
def publish_hello():
    print(request.data['message'])
    sse.publish({"sender": request.data["sender"],
                "message": request.data['message']}, type='message')
    return "Message sent!"