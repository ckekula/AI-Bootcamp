#!/usr/bin/env python3
"""
Task 3: Prompt Templates - Dynamic, Reusable Prompts
Show how ONE template can be reused with different variables.

Learning Goal: Master prompt templates for consistent, reusable prompts.
"""

import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def main():
    print("🎯 Task 3: Dynamic Prompt Templates")
    print("=" * 50)

    print("\n📝 Creating a Reusable Template")
    print("=" * 50)

    # TODO 1: Create a versatile template
    template = PromptTemplate(
        input_variables=["___", "___"],  # Replace ___ with: "topic", "style"
        template="___"  # Replace ___ with: "Explain {topic} in {style}"
    )

    # Test with actual LLM to show it works
    print("\n🤖 Testing Template with AI")
    print("=" * 50)

    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.7
    )

    # TODO 2: Use the template with LLM
    if template and llm:
        # Format the template with specific values
        test_prompt = template.format(
            topic="___",  # Replace ___ with anything (e.g., "quantum computing")
            style="___"  # Replace ___ with any style (e.g., "exactly 5 words")
        )

        print(f"📝 Sending to AI: {test_prompt}")

        # Get AI response
        response = llm.invoke(test_prompt)
        print(f"\n🤖 AI Response: {response.content}")

    # Show the benefits
    print("\n💡 Template Benefits:")
    print("  ✓ ONE template, INFINITE uses")
    print("  ✓ Variables make it dynamic")
    print("  ✓ Consistent structure across all prompts")
    print("  ✓ Change inputs, not code!")

    print("\n✅ Task 3 completed! One template, endless possibilities!")

if __name__ == "__main__":
    main()