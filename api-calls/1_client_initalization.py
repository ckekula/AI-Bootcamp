#!/usr/bin/env python3
"""
Task 2: Initialize the Gemini Client
Learn how to connect to Gemini's servers.
"""

# Step 1: Import the Gemini library
# This library helps us talk to Gemini AI models
import ___ # TODO: Import the google.generativeai library as genai

# Step 2: Import os for environment variables
# This helps us access API keys safely
import ___  # TODO: Import "os"

# The Gemini client needs your API Key (like a password)

# TODO: Initialize the Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("✅ Step 2 Complete: Connected to Gemini!")
print(f"- API Key: {os.getenv('GEMINI_API_KEY')[:10]}...")
