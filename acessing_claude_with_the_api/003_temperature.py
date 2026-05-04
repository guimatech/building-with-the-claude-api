from acessing_claude_with_the_api.common import add_user_message, chat

# A temperature close to 0.0 produces more deterministic, less creative responses,
# while a temperature near 1.0 results in more creative and varied outputs
def main():
    messages = []
    add_user_message(messages, "Generate a one sentence movie idea")
    answer = chat(messages, temperature=0.0)
    print("---")
    print(answer)
    print("---")

    messages = []
    add_user_message(messages, "Generate a one sentence movie idea")
    answer = chat(messages, temperature=1.0)
    print(answer)
    print("---")


if __name__ == "__main__":
    main()