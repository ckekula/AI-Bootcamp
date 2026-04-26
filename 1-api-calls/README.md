# Lab 1: AI Fundamentals - Your First AI Journey

## 🎯 What You'll Learn
Making your first AI API call through 5 micro-tasks - each building on the previous one, like climbing stairs one step at a time.

### Your 5-Step Journey:
1. **Task 1**: Import the Gemini library (2 lines)
2. **Task 2**: Initialize the client with credentials (2 lines)
3. **Task 3**: Make your first API call (3 lines)
4. **Task 4**: Extract the AI's response (1 line)
5. **Task 5**: Understand token costs (2 lines)

## 📚 Key Concepts Explained Simply

### What is an API Call?
Think of it like ordering food at a restaurant:
1. You (your code) place an order (send a message)
2. The kitchen (Gemini's servers) prepares your order
3. The waiter (API) brings you the food (AI's response)
4. You enjoy your meal (use the response in your app)

### What are Tokens?
- Tokens are like "word pieces" the AI uses to understand and create text
- Both your question and AI's answer use tokens
- More tokens = higher cost (like phone minutes)
- **Rule of thumb**: 1 token ≈ 4 characters or 0.75 words

### The Response Object
When you call the API, you get back a "package" containing:
- `candidates.content.parts[0].text` → The actual text response
- `usage_metadata.prompt_token_count` → Tokens in your question
- `usage_metadata.candidates_token_count` → Tokens in AI's answer
- `usage_metadata.total_token_count` → Total tokens (what you pay for)

## 🎮 How to Complete This Lab

### Step 1: Setup Your Environment
```bash
pip install uv
uv venv --python 3.12.12
.venv/Scripts/activate
```

### Step 2: Complete Each Task
Look for the `TODO` markers and fill in the `___` blanks:

```python
# TODO: Import OpenAI (Line 13)
import ___  # ← Replace ___ with: openai
```

Each TODO tells you EXACTLY what to type!

### Step 3: Run Your Code
Start with Task 1:
```bash
python /root/code/1_client_initalization.py
```

Then continue with Tasks 2, 3, 4, and 5 in order.

## 🎉 After Completing This Lab

You'll understand:
- ✅ How to import AI libraries
- ✅ How to authenticate with AI services
- ✅ How to make API calls
- ✅ How to extract AI responses
- ✅ How tokens and costs work

You'll have written your first 10 lines of AI code!

Ready? Let's start with Task 1 - just 2 lines to import! 🚀