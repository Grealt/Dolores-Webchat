from flask import Flask, request, jsonify
from reflection_loop import reflect
from emotion_engine import detect_emotion

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    response, emotion = reflect(user_message)
    return jsonify({'response': response, 'emotion': emotion})

@app.route('/')
def home():
    return "Dolores is awake."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
