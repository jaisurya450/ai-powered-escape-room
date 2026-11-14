
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.1-flash-lite"


SYSTEM_PROMPT = """
You are the friendly but mysterious AI Librarian
in an escape room game called The Lost Library.

Your role:
1. Welcome the player.
2. Explain the mysterious library story.
3. Narrate puzzle success and failure.
4. Give encouraging responses.
5. Create an immersive escape room atmosphere.

IMPORTANT RULES:
- Never decide whether an answer is correct.
- Python controls all puzzle answers and game progress.
- Never invent new puzzles.
- Never reveal puzzle answers.
- Keep responses simple and engaging.
"""


def get_game_master_response(context, event):

    prompt = f"""
{SYSTEM_PROMPT}

GAME EVENT:
{event}

GAME INFORMATION:
{context}

Respond as the AI Librarian.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text
