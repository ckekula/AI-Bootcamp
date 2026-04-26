#!/usr/bin/env python3
"""
Task 3: Making Your First API Call
Understand EVERY part of the chat completion call.
"""

from google import genai
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# ==========================================
# UNDERSTANDING THE API CALL STRUCTURE
# ==========================================
#
# To make a Gemini API call, you:
# 1. Use the client object to access models
# 2. Choose a model (e.g., 'gemini-2.5-flash' or 'gemini-2.5-pro')
# 3. Call the generate_content method with your prompt
#
# ==========================================

# TODO: Fill Uncomment the lines below:

# response = client.models.generate_content(
#     model='gemini-2.5-flash-lite', 
#     contents="Hello AI, please introduce yourself"
# )

# ==========================================
# REAL RESPONSE OBJECT STRUCTURE
# This is an ACTUAL response from OpenAI:
# ==========================================
"""
GenerateContentResponse(
    candidates=[
        Candidate(
            content=Content(
                parts=[Part(text="Hello! I'm Gemini, a large language model trained by Google...")],
                role="model"
            ),
            finish_reason=1,
            index=0,
            safety_ratings=[...]
        )
    ],
    usage_metadata=UsageMetadata(
        prompt_token_count=7,
        candidates_token_count=45,
        total_token_count=52
    )
)
"""

# Once you uncomment and run the code above, this will execute:
try:
    if 'response' in locals() and response:
        # The AI's text shortcut: response.text 
        # Deep path: response.candidates[0].content.parts[0].text
        ai_text = response.text

        print("✅ API Call Successful!")
        print(f"\n🤖 AI said: {ai_text}")
    else:
        print("❌ Complete the code to make your first API call")
except Exception as e:
    print(f"❌ Error: {e}")