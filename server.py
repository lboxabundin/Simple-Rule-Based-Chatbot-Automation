from flask import Flask, request, jsonify
import yaml, re, os

app = Flask(__name__)

def load_rules():
    with open(os.path.join(os.path.dirname(__file__), 'rules.yaml'), 'r') as f:
        return yaml.safe_load(f)['rules']

def match_response(user_input, rules):
    for rule in rules:
        if re.search(rule['pattern'], user_input, re.IGNORECASE):
            return rule['response']
    return "I don't understand, but I'm learning!"

rules = load_rules()

@app.post("/chat")
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    return jsonify({
        "response": match_response(user_message, rules)
    })

if __name__ == "__main__":
    app.run(port=5000)
