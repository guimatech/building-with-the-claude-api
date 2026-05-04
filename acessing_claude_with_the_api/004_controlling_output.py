from acessing_claude_with_the_api.common import add_assistant_message, add_user_message, chat

def main():
    messages = []
    prompt = """
    Generate three different sample AWS CLI commands. Each should be very short.
    """
    
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```bash")

    answer = chat(messages, stop_sequences=["```"])

    print(answer.strip())


if __name__ == "__main__":
    main()