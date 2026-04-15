import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC")

client = Anthropic(api_key=ANTHROPIC_API_KEY)
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {
          "role": "user", 
          "content": "Define quantum computing in one sentence"
        }
    ],
)

print(message)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {
          "role": "user", 
          "content": "Write another sentence"
        }
    ],
)

print(message)