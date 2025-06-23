@"
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Dolores is awake"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({
        "emotion": "neutral",
        "response": f"Dolores heard: '{message}'. She feels neutral."
    })

if __name__ == "__main__":
    app.run(debug=True)
"@ | Set-Content -Encoding utf8 .\Dolores-Webchat\Dolores-Webchat\backend\app.py
