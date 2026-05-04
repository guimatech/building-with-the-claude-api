from acessing_claude_with_the_api.common import add_user_message, chat

def math_tutor_test():
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


def python_dev_test():
    messages = []
    system = """
        You are a Python engineer who writes very concise code.
        """
    
    add_user_message(messages, "Write a Python function that checks a string for duplicate characters.")
    answer = chat(messages, system=system)
    print("---")
    print(answer)
    print("---")

def main():
    python_dev_test()


if __name__ == "__main__":
    main()