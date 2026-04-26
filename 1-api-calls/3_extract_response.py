#!/usr/bin/env python3
"""
Task 4: Extracting the AI's Response
Learn the EXACT path to get the AI's answer from the response object.
"""

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash-lite', 
    contents="What is Python in one sentence?"
)

# ==========================================
# THE MAGIC PATH TO THE AI'S ANSWER
# ==========================================
#
# After making a Gemini API call, the AI's text is ALWAYS at:
# response.candidates[0].content.parts[0].text
#
# Let's understand each part:
# ┌──────────────┐     response: The complete response object from Gemini
# │ response    │
# └─────┬───────┘
#       │
#       ▼
# ┌──────────────┐     .candidates: List of possible responses (usually just one)
# │ .candidates  │
# └─────┬───────┘
#       │
#       ▼
# ┌──────────────┐     [0]: Get the first (and typically only) candidate
# │   [0]        │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .content: The message object containing the response
# │.content │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .parts: List of parts in the message (usually just one)
# │.parts   │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     [0]: Get the first (and typically only) part
# │   [0]   │
# └─────────┘
# ==========================================

# TODO: Extract the AI's text response using the exact path
# Fill in each part of the path:
ai_text = response.___[___].___.___  # TODO: candidates[0].content.parts[0].text

# Display what we extracted
print("🎯 Successfully extracted the AI's response!")
print("\n" + "="*60)
print("Question: What is Python in one sentence?")
print("\nAI's Answer:")
print(ai_text)
print("="*60)

print("\n✅ Task 4 completed! You now know how to extract AI responses!")