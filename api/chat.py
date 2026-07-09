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

        API_KEY = os.environ.get("LLM_API_KEY", "")

        API_URL = "https://api.openai.com/v1/chat/completions"
        TARGET_MODEL = "gpt-4o-mini"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": TARGET_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are Connor. An elite physics intelligence core. Frame separating mass dynamics through strict momentum conservation. Answer directly in clean plaintext prose. Do not use markdown code blocks or LaTeX formatting symbols like $ or $$."
                },
                {"role": "user", "content": user_query}
            ],
            "temperature": 0.05
        }

        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response_json = response.json()

            if "choices" in response_json:
                connor_answer = response_json['choices'][0]['message']['content']
            elif "error" in response_json:
                connor_answer = f"API Provider Error: {response_json['error'].get('message', 'Unknown provider error')}"
            else:
                connor_answer = response_json.get("message", {}).get("content", "Error: Unexpected API response structure.")

        except Exception as e:
            connor_answer = f"Core Fault Intercepted: {str(e)}"

        self.send_response(200)
        self.headers['Content-type'] = 'application/json'
        self.end_headers()

        return_data = {"response": connor_answer}
        self.wfile.write(json.dumps(return_data).encode('utf-8'))