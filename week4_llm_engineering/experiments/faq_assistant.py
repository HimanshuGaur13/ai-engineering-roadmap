from services.llm_service import ask_llm

faq_context = """
Company Knowledge Base

FastAPI:
A modern Python framework for APIs.

Docker:
Containerization platform.

PostgreSQL:
Open-source relational database.
"""


while True:

    question = input("\nAsk FAQ: ")

    if question.lower() == "exit":
        break

    prompt = f"""
    Use ONLY the information below.

    {faq_context}

    Question:
    {question}
    """

    answer = ask_llm(prompt)

    print("\nAnswer:")
    print(answer)