#!/usr/bin/env python3
"""
Task 2: Initialize the Gemini Client
Learn how to connect to Gemini's servers.
"""

# Step 1: Import the Gemini library
# This library helps us talk to Gemini AI models
from google import genai # TODO: Import the genai library from google

# Step 2: Import os and dotenv for environment variables
# This helps us access API keys safely
from dotenv import ___ # TODO: Import "load_dotenv" from "dotenv"

# Load variables from .env file
load_dotenv()

import ___  # TODO: Import "os"

# The Gemini client needs your API Key (like a password)

# TODO: Initialize the Gemini client
api_key = os.getenv("GEMINI_API_KEY")  # Get the API key from environment variables
client = genai.Client(api_key=api_key)

print("✅ Step 2 Complete: Connected to Gemini!")
print(f"- API Key: {api_key[:10]}...")
