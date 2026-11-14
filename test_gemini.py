
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found in .env")

# Connect to Gemini
client = genai.Client(api_key=api_key)

print("Connecting to Gemini AI...")

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents="Create a short mysterious clue for an AI escape room."
    )

    print("\nGemini API Connected Successfully!")
    print("\nAI Escape Room Clue:")
    print(response.text)

except Exception as e:
    print("\nGemini API Error:")
    print(e)

