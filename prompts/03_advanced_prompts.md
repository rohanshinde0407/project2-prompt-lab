# Advanced Prompts (15–21)

**Use Case:** Client Email Drafting
**Author:** Rohan Shinde

---

## Prompt 15
**Technique:** Few-shot prompting

**Prompt:**
```
Below are 2 examples of original emails and their improved versions.
Study the pattern, then improve the new email using the same style.

Example 1:
Original: "Hey, just checking in. Let me know."
Improved: "Hi [Name], I wanted to follow up on our last conversation about [topic]. Could you share your thoughts by [date]? Happy to jump on a quick call if helpful."

Example 2:
Original: "The project is delayed. Sorry."
Improved: "Hi [Name], I wanted to flag that [project] is running approximately [X] days behind schedule due to [reason]. We're taking steps to address this and will have an update by [date]. Please let me know if you'd like to discuss."

Now improve this email:
"The proposal is ready. Check it."
```

**What to observe:** Whether the model follows the pattern from examples
**Edge Cases:** Examples are inconsistent in style
**Failure Modes:** Ignores examples, adds unnecessary padding

---

## Prompt 16
**Technique:** Chain-of-thought prompting

**Prompt:**
```
Think step by step before writing:
1. What is the goal of this email?
2. What tone is appropriate?
3. What key information is missing that you need to assume?
4. Now draft the reply.

Email to reply to:
"We've been evaluating your product for 3 weeks. The team has concerns about integration complexity. We need more clarity before moving forward."
```

**What to observe:** Quality of reasoning steps before the draft
**Edge Cases:** Unclear original email, multiple stakeholders implied
**Failure Modes:** Skips reasoning, overthinks a simple email

---

## Prompt 17
**Technique:** Conditional output handling

**Prompt:**
```
Draft a proposal follow-up email with two versions:
- Version A: Client has viewed the proposal → focus on next steps and scheduling a call
- Version B: Client has NOT viewed the proposal → focus on re-engagement and resending

Label each version clearly.
```

**What to observe:** Whether both cases are genuinely handled differently
**Edge Cases:** Unknown view status (real-world scenario)
**Failure Modes:** Only writes one version, versions are nearly identical

---

## Prompt 18
**Technique:** Multi-step extraction → structured output

**Prompt:**
```
Extract all action items from the email thread below.
Return as a JSON array only, no extra text.
Format: [{"owner": "...", "task": "...", "deadline": "..."}]
If deadline is not specified, use "Not specified".

Email thread: [PASTE THREAD HERE]
```

**What to observe:** Whether it captures all action items accurately
**Edge Cases:** No explicit deadlines, multiple owners for one task
**Failure Modes:** Flat list instead of JSON, misses implicit action items

---

## Prompt 19
**Technique:** Persona + word constraint + personalisation

**Prompt:**
```
You are writing on behalf of Rohan Shinde, a Full Stack Developer with 2 years of experience, now transitioning into AI Engineering.
Write a cold outreach email to a CTO at a mid-size fintech company, pitching AI integration services.
Maximum 100 words. End with a clear, low-friction call to action.
```

**What to observe:** Whether persona + constraint both hold
**Edge Cases:** No target company details, no specific AI service defined
**Failure Modes:** Exceeds word limit, generic pitch, no CTA

---

## Prompt 20
**Technique:** Plain-language transformation

**Prompt:**
```
Rewrite the following technical email so that a non-technical business stakeholder (e.g. a CFO) can fully understand it without any technical background.
Avoid all jargon. Use simple language.

Email: "We've completed the RAG pipeline integration with the vector database. The retrieval latency is now under 200ms P95, and we've added cross-encoder reranking to improve recall. The CI eval pipeline is green. We're ready to push to prod."
```

**What to observe:** Whether ALL jargon is removed, whether meaning is preserved
**Edge Cases:** Some technical terms have no simple equivalent
**Failure Modes:** Still uses technical terms, loses key meaning in simplification

---

## Prompt 21
**Technique:** Predictive / proactive prompting

**Prompt:**
```
Below is an email thread between our team and a client (3 messages).
Based on the conversation history, predict what the client is most likely to ask or say next.
Then draft a proactive reply that addresses that likely question before they ask it.

Thread:
Message 1 (Us): "Here is the proposal for Phase 1 of the AI integration project."
Message 2 (Client): "Thanks, looks interesting. What does the timeline look like?"
Message 3 (Us): "Phase 1 is 6 weeks, starting from contract sign-off."
```

**What to observe:** Quality of prediction, relevance of proactive reply
**Edge Cases:** Ambiguous conversation history, multiple possible next questions
**Failure Modes:** Predicts wrong intent, proactive reply misses the point
