# this is to test with a UI

from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize the chatbot
chatbot = ChatBot(api_key=os.getenv("GENAI_API_KEY"))
chatbot.start_conversation()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    user_input = request.json.get("prompt")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        response = chatbot.send_prompt(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
