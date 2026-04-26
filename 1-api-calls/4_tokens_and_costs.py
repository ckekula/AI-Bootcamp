#!/usr/bin/env python3
"""
Task 5: Understanding Tokens and Business Costs
Learn how tokens work and calculate real business costs for AI usage.
"""

from google import genai
import os

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash-lite', 
    contents="Explain the benefits of using AI for customer support in a business"
)

# ==========================================
# WHAT ARE TOKENS?
# ==========================================
#
# Think of tokens as "pieces of words" that AI uses:
# - Simple words = 1 token (e.g., "cat", "run")
# - Complex words = multiple tokens (e.g., "unbelievable" = 3 tokens)
# - Rough estimate: 1 token ≈ 4 characters or 0.75 words
#
# The response.usage_metadata object tells you EXACTLY how many tokens you used:
# ┌────────────────────────────────────┐
# │ response.usage_metadata             │
# │  ├── prompt_token_count      (input)    │ ← What you asked
# │  ├── candidates_token_count  (output)   │ ← What AI answered
# │  └── total_token_count       (sum)      │ ← What you pay for
# └────────────────────────────────────┘
# ==========================================

# TODO: Extract the token counts from response.usage_metadata
metadata = response.usage_metadata
input_tokens = metadata.prompt_token_count
output_tokens = metadata.candidates_token_count
total_tokens = metadata.total_token_count

print("📊 Token Usage Report:")
print("="*50)
print(f"  Your question used: {input_tokens} tokens")
print(f"  AI's response used: {output_tokens} tokens")
print(f"  Total tokens billed: {total_tokens} tokens")
print("="*50)

# ==========================================
# CALCULATING REAL BUSINESS COSTS (Gemini 2.5 Flash)
# ==========================================
# 
# Note: Gemini 2.5 Flash is significantly cheaper than GPT-4.
# Current Flash Pricing (for prompts under 128k tokens):
# Input:  ~$0.1 per 1M tokens ($0.000075 per 1K)
# Output: ~$0.4  per 1M tokens ($0.0003   per 1K)
# ==========================================

# Gemini 2.5 Flash pricing (per 1M tokens)
input_price_per_1m = 0.1
output_price_per_1m = 0.4

# Calculate actual costs
input_cost = (input_tokens / 1000000) * input_price_per_1m
output_cost = (output_tokens / 1000000) * output_price_per_1m
total_cost = input_cost + output_cost

print("\n💰 Cost Breakdown for This Call:")
print("-"*50)
print(f"  Input cost:  ${input_cost:.6f} ({input_tokens} tokens)")
print(f"  Output cost: ${output_cost:.6f} ({output_tokens} tokens)")
print(f"  TOTAL COST:  ${total_cost:.6f}")
print("-"*50)

print("\n✅ Task 5 completed! You now understand Gemini tokens and costs!")