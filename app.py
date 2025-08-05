import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Set your GEMINI_API_KEY in .env!")

genai.configure(api_key=api_key)

def ask_gemini(prompt, model_name='gemini-1.5-flash'):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text

@app.route("/api/justicemate", methods=["POST"])
def justicemate():
    data = request.json
    issue_type = data.get("help_type", "rights")  # or send as 'type' from frontend
    user_input = data.get("issue_description", "")
    result = ""

    if issue_type == "rights":
        prompt = f"Summarize the user's legal rights under Indian law in plain language:\n{user_input}"
        result = ask_gemini(prompt)
    elif issue_type == "complaint":
        prompt = f"Draft a formal complaint letter for the following issue in Indian context:\n{user_input}"
        result = ask_gemini(prompt)
    elif issue_type == "mediation":
        prompt = (
            f"Party 1: {user_input}\n"
            f"Party 2: {data.get('opposing_party','(not provided)')}\n"
            "Summarize positions and suggest a fair, practical mediation solution."
        )
        result = ask_gemini(prompt)
    elif issue_type == "legalese-to-plain":
        prompt = f"Translate this legalese into plain, easy-to-understand language:\n\n{user_input}"
        result = ask_gemini(prompt)
    else:
        result = "Unknown help type."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
