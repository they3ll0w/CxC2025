from flask import Flask, request, jsonify
from groq import Groq
from flask_cors import CORS
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()

@app.route('/api/llm', methods=['POST'])
def llm():
    data = request.get_json()
    prompt = data.get('input', '')
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=600,
        top_p=0.65,
        stream=True,
        stop=None,
    )
    response = ""
    for chunk in completion:
        response = response + (chunk.choices[0].delta.content or "")
    return response

if __name__ == '__main__':
    app.run(debug=True)
