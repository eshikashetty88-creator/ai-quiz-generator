import json
import os

FILE = "progress.json"

def save_progress(score, topic):
    data = load_progress()
    data.append({"score": score, "topic": topic})
    with open(FILE, "w") as f:
        json.dump(data, f)

def load_progress():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)