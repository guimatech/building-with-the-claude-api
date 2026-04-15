import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC")

model = "claude-sonnet-4-6"
client = Anthropic(api_key=ANTHROPIC_API_KEY)

def add_user_message(messages, text):
    messages.append({
        "role": "user",
        "content": text
    })

def add_assistant_message(messages, text):
    messages.append({
        "role": "assistant",
        "content": text
    })

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1024,
        "messages": messages,
    }
    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text