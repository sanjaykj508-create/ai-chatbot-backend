from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types
import os
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# Gemini API client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Store conversation history
conversations = {}

# Context window management
# Only the latest 10 messages are sent to Gemini
MAX_MESSAGES = 10

# System prompt
SYSTEM_PROMPT = """
You are KJ Assistant, a friendly and helpful AI chatbot.

Your purpose is to help users with:
- Python programming
- Data analysis
- AI and machine learning
- Career and interview preparation

Be clear, beginner-friendly, and concise.
If you don't know something, say so instead of making up information.
"""


@app.get("/")
def home():
    return {
        "message": "AI Chatbot Backend is Working!"
    }


@app.get("/chat")
def chat(conversation_id: str, message: str):

    try:

        # Create conversation if it doesn't exist
        if conversation_id not in conversations:
            conversations[conversation_id] = []

        history = conversations[conversation_id]

        # Add user message
        history.append({
            "role": "user",
            "text": message
        })

        # Context window management
        # Keep only the latest 10 messages
        history = history[-MAX_MESSAGES:]

        # Convert history to Gemini format
        contents = []

        for item in history:

            role = item["role"]

            # Gemini uses "model" instead of "assistant"
            if role == "assistant":
                role = "model"

            contents.append(
                types.Content(
                    role=role,
                    parts=[
                        types.Part(
                            text=item["text"]
                        )
                    ]
                )
            )

        # Retry API request up to 3 times
        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    )
                )

                break

            except Exception as e:

                print(
                    f"Gemini error (attempt {attempt + 1}): {e}"
                )

                if attempt == max_retries - 1:

                    raise HTTPException(
                        status_code=503,
                        detail="Gemini service is temporarily unavailable. Please try again later."
                    )

                # Exponential backoff
                time.sleep(2 ** attempt)

        # Get AI response
        assistant_message = response.text

        # Store AI response
        history.append({
            "role": "assistant",
            "text": assistant_message
        })

        # Keep only latest 10 messages
        conversations[conversation_id] = history[-MAX_MESSAGES:]

        return {
            "conversation_id": conversation_id,
            "response": assistant_message,
            "context_window": "Latest 10 messages maintained"
        }

    except HTTPException:
        raise

    except Exception as e:

        print(f"Unexpected error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Something went wrong. Please try again."
        )