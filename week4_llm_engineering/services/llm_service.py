from google import genai
from config.settings import GEMINI_API_KEY
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_llm(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"LLM Error: {str(e)}"