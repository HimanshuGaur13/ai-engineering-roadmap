from services.llm_service import ask_llm
#  to run this file--- python3 -m experiments.chatbot
print("AI Chatbot")
print("Type 'exit' to quit\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = ask_llm(user_input)

    print("\nAI:", response)
    print()