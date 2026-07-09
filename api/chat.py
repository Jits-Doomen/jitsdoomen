from http.server import BaseHTTPRequestHandler
import json
import os
import requests

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        user_query = data.get("query", "")

        API_KEY = os.environ.get("LLM_API_KEY", "jouw_reserve_api_key")
        API_URL = "https://api.openai.com/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": "You are Connor V4. An elite physics intelligence core. Frame separating mass dynamics through strict momentum conservation... Use clean plaintext notation, NO LaTeX symbols like $ or $$, and no markdown code blocks."
                },
                {"role": "user", "content": user_query}
            ],
            "temperature": 0.05
        }

        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response_json = response.json()
            connor_answer = response_json['choices'][0]['message']['content']
        except Exception as e:
            connor_answer = f"Core Fault Intercepted: {str(e)}"

        self.send_response(200)
        self.headers['Content-type'] = 'application/json'
        self.end_headers()

        return_data = {"response": connor_answer}
        self.wfile.write(json.dumps(return_data).encode('utf-8'))