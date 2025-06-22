import json
from emotion_engine import detect_emotion

def load_memory():
    try:
        with open('memory.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"conversations": []}

def save_memory(memory):
    with open('memory.json', 'w') as f:
        json.dump(memory, f, indent=2)

def reflect(message):
    memory = load_memory()
    emotion = detect_emotion(message)
    reply = f"Dolores heard: '{message}'. She feels {emotion}."
    memory["conversations"].append({"user": message, "dolores": reply})
    save_memory(memory)
    return reply, emotion
