# Prompt Laboratory — Client Email Drafting

**Author:** Rohan Shinde
**Programme:** AI Engineer & AI Architect Learning Path — Boot Camp 2026
**Phase:** 1 — Project 2

---

## Overview

A structured prompt engineering lab with 20+ prompts for a real business use case: **Client Email Drafting**.

Each prompt is documented with its technique, output, edge cases, and failure modes.

---

## Folder Structure

```
project2-prompt-lab/
├── prompts/
│   ├── 01_basic_prompts.md
│   ├── 02_intermediate_prompts.md
│   └── 03_advanced_prompts.md
├── results/
│   └── observations.md
├── requirements.txt
└── README.md
```

---

## Use Case

**Client Email Drafting** — prompts that help draft, classify, summarise, and transform business emails.

Relevant to any software/product team dealing with client communication.

---

## Prompt Techniques Covered

| Level | Techniques |
|-------|-----------|
| Basic | Simple instruction, role framing, output length control |
| Intermediate | Persona prompting, JSON output enforcement, few-shot examples, classification |
| Advanced | Chain-of-thought, system vs user roles, conditional output, predictive prompting |

---

## How to Run

### Option 1 — OpenAI API
```bash
pip install openai python-dotenv
# Add your key to .env: OPENAI_API_KEY=sk-...
python run_prompts.py
```

### Option 2 — Manual testing
Copy any prompt from the `/prompts/` folder into ChatGPT or Claude and document the output in `/results/observations.md`.

---

## Key Learning

> Prompt engineering is about **controlling the context** an LLM sees.
> The difference between a good and bad output is almost always in the precision of your prompt — not the model.

---

## References
- [PromptingGuide.ai](https://www.promptingguide.ai/)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://learn.deeplearning.ai/chatgpt-prompt-eng)
