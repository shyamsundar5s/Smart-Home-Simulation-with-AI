# Smart-Home-Simulation-with-AI
This project is a **Smart Home System** that simulates and automates the control of devices based on user behavior, time of day, and environmental factors. It is designed to learn user preferences and patterns to efficiently manage smart devices in a home environment.
## 🔧 Core Features
### 🏠 Simulated Smart Devices
1. **Lights**:
   - On/Off
   - Adjustable dim level
2. **Fan / AC**:
   - On/Off
   - Adjustable speed/temperature
3. **Sensors**:
   - Motion Sensor
   - Temperature Sensor (simulated or hardware-based)

## 📊 Inputs
1. **Time of Day**
2. **Day of the Week**
3. **Room Temperature**
4. **Motion Detected**
5. **User’s Past Device Usage**

## 🔁 Outputs
1. **AI-driven Decisions**:
   - Example: "Turn on AC at 28°C if motion is detected after 4 PM."
2. **Manual Override**:
   - Users can manually control devices via a web dashboard.

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Framework**: Flask/Django for the web dashboard
- **Machine Learning**: Scikit-learn (Random Forest, Decision Trees)
- **Communication**: MQTT / Serial Communication (to integrate with Raspberry Pi/NodeMCU)
- **Data Visualization**: Matplotlib / Plotly
- **Database**: SQLite / Firebase for logs

## 🔄 How It Works
1. **Simulated or Real Sensor Data**:
   - Uses random inputs or live sensor data from microcontrollers like Raspberry Pi.
2. **User Behavior Logger**:
   - Logs when users turn devices on/off.
3. **Training the Model**:
   - Trains an ML model to predict actions based on context (time, temp, motion).
4. **Automation Engine**:
   - The ML model decides whether to trigger a device automatically.
5. **Web Dashboard**:
   - Displays live device status, analytics, and provides options for manual control.

## 🚀 Bonus Features
- **Voice Assistant**:
  - Integrate with Python’s SpeechRecognition library for voice commands.
- **Mobile Interface**:
  - Flask + responsive UI for better accessibility.
- **Energy Consumption Tracking**:
  - Generate efficiency reports for users.
- **Predictive Maintenance Alerts**:
  - Notify users about potential issues with devices.

## 📂 Project Structure
smart-home-simulation/
├── app.py                    
├── templates/
│   └── dashboard.html       
├── static/
│   └── style.css             
├── models/
│   ├── prediction_model.py   
│   └── data_logger.py        
├── database/
│   └── smart_home.db         
├── sensors/
│   ├── motion_sensor.py      
│   └── temperature_sensor.py 
└── README.md                 
