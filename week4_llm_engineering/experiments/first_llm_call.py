# from services.llm_service import ask_llm
# from prompt.prompts import SYSTEM_PROMPT

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     response = ask_llm(user_input)

#     print("\nAI:", response)
from services.llm_service import ask_llm

response = ask_llm(
    "Explain FastAPI in simple terms."
)

print(response)