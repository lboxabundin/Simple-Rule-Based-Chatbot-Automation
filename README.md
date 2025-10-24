# Simple Rule-Based Chatbot 🤖

A lightweight open-source chatbot and automation system based on **pattern matching rules**.  
Can be used as a **support bot**, **FAQ responder**, or **automation trigger bot**.

## Features
- Rule-based message matching
- YAML configuration for conversation logic
- CLI mode for local chatting
- Webhook server mode (Flask) for integration with messaging platforms
- Easy to customize and extend

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### 1. Run in CLI mode
```bash
python -m simple_chatbot.cli
```

### 2. Run as Webhook Server (for integration)
```bash
python -m simple_chatbot.server
```
Server runs on: `http://localhost:5000/chat`

Send a POST request:
```json
{ "message": "hello" }
```

### 3. Edit conversation rules
Open `rules.yaml` and modify patterns and responses.

## Sponsor ❤️
If this project helped you, consider supporting ongoing development.

## License
MIT
