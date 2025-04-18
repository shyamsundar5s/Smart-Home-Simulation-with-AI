from sklearn.ensemble import RandomForestClassifier
import sqlite3

# Initialize the model
model = RandomForestClassifier()
training_data = []
labels = []

def train_model():
    global training_data, labels
    # Add dummy data
    training_data.extend([
        [12, 1, 28.0, 1],  # [time_of_day, day_of_week, temperature, motion_detected]
        [18, 4, 24.5, 1],
        [22, 6, 30.2, 0],
    ])
    labels.extend([1, 0, 0])  # Actions: 1 = Turn AC on, 0 = Turn AC off
    if training_data and labels:
        model.fit(training_data, labels)

def predict_action(context):
    return model.predict([context])[0]
