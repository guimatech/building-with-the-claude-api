from acessing_claude_with_the_api.common import add_user_message, add_assistant_message, chat

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