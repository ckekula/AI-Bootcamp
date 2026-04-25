#!/usr/bin/env python3
"""
Task 5: Understanding Tokens and Business Costs
Learn how tokens work and calculate real business costs for AI usage.
"""

import google.generativeai as genai
import os

# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Make an API call with a business-relevant prompt
prompt = "Explain the benefits of using AI for customer support in a business"
response = model.generate_content(prompt)

# ==========================================
# WHAT ARE TOKENS?
# ==========================================
#
# Think of tokens as "pieces of words" that AI uses:
# - Simple words = 1 token (e.g., "cat", "run")
# - Complex words = multiple tokens (e.g., "unbelievable" = 3 tokens)
# - Rough estimate: 1 token ≈ 4 characters or 0.75 words
#
# The response.usage object tells you EXACTLY how many tokens you used:
# ┌────────────────────────────────────┐
# │ response.usage                      │
# │  ├── prompt_tokens      (input)    │ ← What you asked
# │  ├── completion_tokens  (output)   │ ← What AI answered
# │  └── total_tokens       (sum)      │ ← What you pay for
# └────────────────────────────────────┘
# ==========================================

# TODO: Extract the token counts from response.usage_metadata
input_tokens = response.usage_metadata.prompt_token_count
output_tokens = response.usage_metadata.candidates_token_count
total_tokens = response.usage_metadata.total_token_count

print("📊 Token Usage Report:")
print("="*50)
print(f"  Your question used: {input_tokens} tokens")
print(f"  AI's response used: {output_tokens} tokens")
print(f"  Total tokens billed: {total_tokens} tokens")
print("="*50)

# ==========================================
# CALCULATING REAL BUSINESS COSTS (Gemini 1.5 Flash)
# ==========================================
# 
# Note: Gemini 1.5 Flash is significantly cheaper than GPT-4.
# Current Flash Pricing (for prompts under 128k tokens):
# Input:  ~$0.075 per 1M tokens ($0.000075 per 1K)
# Output: ~$0.30  per 1M tokens ($0.0003   per 1K)
# ==========================================

# Gemini 1.5 Flash pricing (per 1,000 tokens)
input_price_per_1k = 0.000075
output_price_per_1k = 0.0003

# Calculate actual costs
input_cost = (input_tokens / 1000) * input_price_per_1k
output_cost = (output_tokens / 1000) * output_price_per_1k
total_cost = input_cost + output_cost

print("\n💰 Cost Breakdown for This Call:")
print("-"*50)
print(f"  Input cost:  ${input_cost:.6f} ({input_tokens} tokens)")
print(f"  Output cost: ${output_cost:.6f} ({output_tokens} tokens)")
print(f"  TOTAL COST:  ${total_cost:.6f}")
print("-"*50)

print("\n✅ Task 5 completed! You now understand Gemini tokens and costs!")