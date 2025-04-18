# Import necessary libraries
import random
from datetime import datetime
import sqlite3
from flask import Flask, render_template, request, jsonify
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt

# Initialize Flask app
app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('smart_home.db', check_same_thread=False)
cursor = conn.cursor()

# Create tables for logs and user behavior
cursor.execute('''
CREATE TABLE IF NOT EXISTS device_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device TEXT,
    action TEXT,
    timestamp DATETIME,
    context TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS user_behavior (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_of_day INTEGER,
    day_of_week INTEGER,
    temperature REAL,
    motion_detected INTEGER,
    action INTEGER
)
''')
conn.commit()

# Simulated sensors and devices
class SmartHome:
    def __init__(self):
        self.lights = {'status': 'off', 'dim_level': 0}
        self.ac = {'status': 'off', 'temperature': 24}
        self.motion_detected = False
        self.temperature = 25

    def update_sensors(self):
        self.motion_detected = random.choice([True, False])
        self.temperature = random.uniform(20, 35)

smart_home = SmartHome()

# Machine Learning Model
model = RandomForestClassifier()
training_data = []
labels = []

def train_model():
    global training_data, labels
    if training_data and labels:
        model.fit(training_data, labels)

# Train model with initial dummy data
dummy_data = [
    [12, 1, 28.0, 1],  # [time_of_day, day_of_week, temperature, motion_detected]
    [18, 4, 24.5, 1],
    [22, 6, 30.2, 0]
]
dummy_labels = [1, 0, 0]  # Actions: 1 = Turn AC on, 0 = Turn AC off
training_data.extend(dummy_data)
labels.extend(dummy_labels)
train_model()

# Predict action based on input context
def predict_action(context):
    return model.predict([context])[0]

# Web dashboard routes
@app.route('/')
def home():
    return render_template('dashboard.html', devices=smart_home.__dict__)

@app.route('/update_sensors', methods=['POST'])
def update_sensors():
    smart_home.update_sensors()
    return jsonify({'motion_detected': smart_home.motion_detected, 'temperature': smart_home.temperature})

@app.route('/control_device', methods=['POST'])
def control_device():
    device = request.json['device']
    action = request.json['action']
    context = {
        'time_of_day': datetime.now().hour,
        'day_of_week': datetime.now().weekday(),
        'temperature': smart_home.temperature,
        'motion_detected': int(smart_home.motion_detected)
    }
    cursor.execute('''
        INSERT INTO device_logs (device, action, timestamp, context)
        VALUES (?, ?, ?, ?)
    ''', (device, action, datetime.now(), str(context)))
    conn.commit()
    # Update device status
    if device == 'lights':
        smart_home.lights['status'] = action
    elif device == 'ac':
        smart_home.ac['status'] = action
    return jsonify({'status': 'success'})

@app.route('/ai_action', methods=['POST'])
def ai_action():
    context = [
        datetime.now().hour,
        datetime.now().weekday(),
        smart_home.temperature,
        int(smart_home.motion_detected)
    ]
    action = predict_action(context)
    # Log and update device
    cursor.execute('''
        INSERT INTO user_behavior (time_of_day, day_of_week, temperature, motion_detected, action)
        VALUES (?, ?, ?, ?, ?)
    ''', (*context, action))
    conn.commit()
    return jsonify({'ai_action': action})

@app.route('/analytics', methods=['GET'])
def analytics():
    cursor.execute('SELECT * FROM device_logs')
    logs = cursor.fetchall()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
