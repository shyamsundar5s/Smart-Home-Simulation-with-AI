CREATE TABLE IF NOT EXISTS device_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device TEXT,
    action TEXT,
    timestamp DATETIME,
    context TEXT
);

CREATE TABLE IF NOT EXISTS user_behavior (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_of_day INTEGER,
    day_of_week INTEGER,
    temperature REAL,
    motion_detected INTEGER,
    action INTEGER
);
