#!/usr/bin/env python3
"""
Task 3: Making Your First API Call
Understand EVERY part of the chat completion call.
"""

import google.generativeai as genai
import os

# Initialize client
# Note: Gemini uses genai.configure instead of a client object instantiation
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ==========================================
# UNDERSTANDING THE API CALL STRUCTURE
# ==========================================
#
# To make a Gemini API call, you:
# 1. Initialize a model using genai.GenerativeModel('model-name')
# 2. Call generate_content()
#
# Gemini models: "gemini-1.5-flash" (fast) or "gemini-1.5-pro" (powerful)
# ==========================================

# TODO: Fill in the blanks and uncomment the lines below:

# model = genai.GenerativeModel('gemini-1.5-flash')

# response = model.generate_content("Hello AI, please introduce yourself")

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
        print(f"\n📊 Total tokens used: {response.usage_metadata.total_token_count}")

        # Create marker
        os.makedirs("/root/markers", exist_ok=True)
        with open("/root/markers/task3_api_call_complete.txt", "w") as f:
            f.write("SUCCESS")
    else:
        print("❌ Complete the code to make your first API call")
except Exception as e:
    print(f"❌ Error: {e}")