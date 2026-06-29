from services.llm_service import ask_llm
import json

prompt = """
Extract skills from the following text.

Return ONLY JSON.

Text:
Python, FastAPI, PostgreSQL, Docker

Format:
{
    "skills":[]
}
"""

response = ask_llm(prompt)

print(response)

try:
    data = json.loads(response)
    print("\nParsed JSON:")
    print(data)

except Exception as e:
    print("JSON Parsing Error:", e)