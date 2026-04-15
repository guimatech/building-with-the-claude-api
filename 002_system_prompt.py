from common import add_user_message, add_assistant_message, chat

def main():
    messages = []
    system = """
        You are a patient math tutor.
        Do not directly answer a student's questions.
        Guide them to a solution step by step.
        """
    
    add_user_message(messages, "How do I solve 5x+3=2 for x?")
    answer = chat(messages, system=system)
    print("---")
    print(answer)
    print("---")


if __name__ == "__main__":
    main()