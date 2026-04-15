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

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=messages,
    )
    return message.content[0].text

def main():
    messages = []

    add_user_message(messages, "Define quantum computing in one sentence")
    answer = chat(messages)
    print(answer)

    add_assistant_message(messages, answer)
    print(messages)

    add_user_message(messages, "Write another sentence")
    answer = chat(messages)
    print(answer)

if __name__ == "__main__":
    main()