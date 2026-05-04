from acessing_claude_with_the_api.common import client, model, add_user_message, chat

def main():
    messages = []
    add_user_message(messages, "Write a 1 sentence description of a fake database")

    with client.messages.create({
        "model": model,
        "max_tokens": 1024,
        "messages": messages,
        "stream": True
    }) as stream:
        for text in stream.text_stream:
            print(text, end="")
            # pass

    # stream.get_final_message()


if __name__ == "__main__":
    main()