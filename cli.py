import yaml
import re
import os

def load_rules():
    with open(os.path.join(os.path.dirname(__file__), 'rules.yaml'), 'r') as f:
        return yaml.safe_load(f)['rules']

def match_response(user_input, rules):
    for rule in rules:
        if re.search(rule['pattern'], user_input, re.IGNORECASE):
            return rule['response']
    return "I don't understand, but I'm learning!"

def main():
    rules = load_rules()
    print("🤖 Simple Chatbot — type 'exit' to quit")
    while True:
        user = input("> ")
        if user.lower() == "exit":
            break
        print(match_response(user, rules))

if __name__ == "__main__":
    main()
