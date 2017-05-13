from flask import Flask, render_template, request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://redis-18275.c11.us-east-1-3.ec2.cloud.redislabs.com:18275"
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