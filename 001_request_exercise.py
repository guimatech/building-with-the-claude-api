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
    while True:
        user_input = input("> ")
        print(">", user_input)

        add_user_message(messages, user_input)
        answer = chat(messages)
        add_assistant_message(messages, answer)
        print("---")
        print(answer)
        print("---")


if __name__ == "__main__":
    main()