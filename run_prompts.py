"""
Prompt Lab Runner — Phase 1 Project 2
Author: Rohan Shinde
Programme: AI Engineer & AI Architect Learning Path — Boot Camp 2026

Run any prompt from the lab against the OpenAI API and log results.

Usage:
    pip install openai python-dotenv
    Add OPENAI_API_KEY=sk-... to a .env file
    python run_prompts.py
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ─────────────────────────────────────────────────────────────
# Sample prompts to test (add your own from the /prompts/ folder)
# ─────────────────────────────────────────────────────────────

PROMPTS = [
    {
        "id": 1,
        "technique": "Simple instruction",
        "prompt": "Write a follow-up email to a client who hasn't replied in 5 days."
    },
    {
        "id": 10,
        "technique": "JSON output enforcement",
        "prompt": (
            'Return ONLY a valid JSON object with no extra text, no markdown, no explanation.\n'
            'Format: {"subject": "...", "body": "...", "tone": "..."}\n\n'
            'Task: Write a re-engagement email to a client who has been dormant for 3 months.'
        )
    },
    {
        "id": 16,
        "technique": "Chain-of-thought",
        "prompt": (
            "Think step by step before writing:\n"
            "1. What is the goal of this email?\n"
            "2. What tone is appropriate?\n"
            "3. What key information is missing that you need to assume?\n"
            "4. Now draft the reply.\n\n"
            'Email to reply to:\n"We\'ve been evaluating your product for 3 weeks. '
            'The team has concerns about integration complexity. We need more clarity before moving forward."'
        )
    },
]


def run_prompt(prompt_data: dict) -> str:
    """Send a prompt to the OpenAI API and return the response."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt_data["prompt"]}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content


def main():
    print("=" * 60)
    print("  Prompt Laboratory — Client Email Drafting")
    print("  Author: Rohan Shinde")
    print("=" * 60)

    for p in PROMPTS:
        print(f"\n{'─' * 60}")
        print(f"Prompt #{p['id']} — Technique: {p['technique']}")
        print(f"{'─' * 60}")
        print(f"PROMPT:\n{p['prompt']}\n")

        try:
            result = run_prompt(p)
            print(f"OUTPUT:\n{result}")
        except Exception as e:
            print(f"ERROR: {e}")

        print()

    print("=" * 60)
    print("✅ Lab run complete. Document your observations in results/observations.md")


if __name__ == "__main__":
    main()
