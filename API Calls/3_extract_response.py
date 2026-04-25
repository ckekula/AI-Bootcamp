#!/usr/bin/env python3
"""
Task 4: Extracting the AI's Response
Learn the EXACT path to get the AI's answer from the response object.
"""

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Make a simple API call to get a response
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is Python in one sentence?")

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
# ┌─────────┐     .message: The message object containing the response
# │.message │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .content: The actual text string from the AI!
# │.content │
# └─────────┘
# ==========================================

# TODO: Extract the AI's text response using the exact path
# Fill in each part of the path:
ai_text = response.___[___].___.___  # TODO: choices[0].message.content

# Display what we extracted
print("🎯 Successfully extracted the AI's response!")
print("\n" + "="*60)
print("Question: What is Python in one sentence?")
print("\nAI's Answer:")
print(ai_text)
print("="*60)

print("\n✅ Task 4 completed! You now know how to extract AI responses!")