import sqlite3
from datetime import datetime

DATABASE = "database/smart_home.db"

def log_device_action(device, action, context):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO device_logs (device, action, timestamp, context)
        VALUES (?, ?, ?, ?)
    ''', (device, action, datetime.now(), str(context)))
    conn.commit()
    conn.close()

def get_device_logs():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM device_logs')
    logs = cursor.fetchall()
    conn.close()
    return logs
