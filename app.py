from flask import Flask, render_template, request, jsonify
from models.prediction_model import train_model, predict_action
from models.data_logger import log_device_action, get_device_logs
from sensors.motion_sensor import get_motion_status
from sensors.temperature_sensor import get_room_temperature
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Simulated devices
smart_home = {
    "lights": {"status": "off", "dim_level": 0},
    "ac": {"status": "off", "temperature": 24},
}

@app.route("/")
def dashboard():
    return render_template("dashboard.html", devices=smart_home)

@app.route("/update_sensors", methods=["POST"])
def update_sensors():
    motion_status = get_motion_status()
    room_temperature = get_room_temperature()
    return jsonify({"motion_detected": motion_status, "temperature": room_temperature})

@app.route("/control_device", methods=["POST"])
def control_device():
    data = request.json
    device = data.get("device")
    action = data.get("action")
    context = {
        "time_of_day": datetime.now().hour,
        "day_of_week": datetime.now().weekday(),
        "temperature": get_room_temperature(),
        "motion_detected": int(get_motion_status()),
    }
    log_device_action(device, action, context)
    if device in smart_home:
        smart_home[device]["status"] = action
    return jsonify({"status": "success"})

@app.route("/ai_action", methods=["POST"])
def ai_action():
    context = [
        datetime.now().hour,
        datetime.now().weekday(),
        get_room_temperature(),
        int(get_motion_status()),
    ]
    action = predict_action(context)
    return jsonify({"ai_action": action})

@app.route("/analytics", methods=["GET"])
def analytics():
    logs = get_device_logs()
    return jsonify(logs)

if __name__ == "__main__":
    train_model()
    app.run(debug=True)
