# Intermediate Prompts (8–14)

**Use Case:** Client Email Drafting
**Author:** Rohan Shinde

---

## Prompt 8
**Technique:** Persona prompting

**Prompt:**
```
You are a senior account manager at a B2B SaaS company.
Write a follow-up email to a client after a product demo. Tone: warm but professional.
```

**What to observe:** How much the persona shifts the output vs a plain instruction
**Edge Cases:** Client name unknown, no demo details given
**Failure Modes:** Sounds too salesy, ignores the persona instruction

---

## Prompt 9
**Technique:** Diplomatic framing

**Prompt:**
```
Write an email politely declining a client's feature request.
Acknowledge their need, explain why it's not on the current roadmap, and offer an alternative timeline of Q3 next year.
```

**What to observe:** Diplomacy level, whether it maintains the relationship
**Edge Cases:** No feature details provided
**Failure Modes:** Too blunt, no alternative offered

---

## Prompt 10
**Technique:** JSON output enforcement

**Prompt:**
```
Return ONLY a valid JSON object with no extra text, no markdown, no explanation.
Format: {"subject": "...", "body": "...", "tone": "..."}

Task: Write a re-engagement email to a client who has been dormant for 3 months.
```

**What to observe:** Whether the output is clean, parseable JSON
**Edge Cases:** Model adds backticks or explanation outside JSON
**Failure Modes:** Extra text outside JSON, invalid JSON format

---

## Prompt 11
**Technique:** Multi-variation output

**Prompt:**
```
Write 3 variations of a cold outreach email to a CTO about our AI product.
Label each: [Formal], [Casual], [Bold].
Each must be under 80 words.
```

**What to observe:** Whether the 3 tones are genuinely different
**Edge Cases:** No product context given
**Failure Modes:** All 3 sound the same, exceeds word limit

---

## Prompt 12
**Technique:** Classification with output control

**Prompt:**
```
Classify the following email into exactly one category: Urgent / Follow-up / Informational.
Return only the single word label. No explanation.

Email: [PASTE EMAIL HERE]
```

**What to observe:** Whether it returns ONLY the label
**Edge Cases:** Ambiguous email that could fit two categories
**Failure Modes:** Returns explanation instead of label, creates a new category

---

## Prompt 13
**Technique:** Structured data extraction

**Prompt:**
```
Extract the following fields from the email below and return as JSON only.
Format: {"client_name": "...", "deadline": "...", "requested_action": "..."}
If a field is not found, use null.

Email: [PASTE EMAIL HERE]
```

**What to observe:** Extraction accuracy, handling of missing fields
**Edge Cases:** Multiple deadlines, implied (not explicit) actions
**Failure Modes:** Misses nested info, returns string instead of JSON

---

## Prompt 14
**Technique:** Role-based prompting (system + user separation)

**Prompt:**
```
System: You are an AI email assistant for a B2B SaaS company. 
You always write in a professional tone, keep emails under 150 words, and end with a clear call to action.

User: Draft a contract renewal reminder for a client whose contract expires in 30 days.
```

**What to observe:** Whether the system instruction shapes the output consistently
**Edge Cases:** No contract value given, no client name
**Failure Modes:** Ignores system context, exceeds word limit
