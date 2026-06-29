from services.llm_service import ask_llm

prompt = """
You are an AI router.

If user asks about weather:

Return:

{
    "function":"get_weather",
    "city":"CITY_NAME"
}

User:
What is the weather in Delhi?

Return ONLY JSON.
"""

response = ask_llm(prompt)

print(response)