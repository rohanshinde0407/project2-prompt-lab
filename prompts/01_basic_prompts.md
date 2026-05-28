# Basic Prompts (1–7)

**Use Case:** Client Email Drafting
**Author:** Rohan Shinde

---

## Prompt 1
**Technique:** Simple instruction

**Prompt:**
```
Write a follow-up email to a client who hasn't replied in 5 days.
```

**What to observe:** Tone, length, whether it sounds professional
**Edge Cases:** No client name given, no context about what was sent
**Failure Modes:** Too aggressive, too generic, no clear CTA

---

## Prompt 2
**Technique:** Simple instruction + output constraint

**Prompt:**
```
Write a short intro email (max 100 words) introducing our software product to a new lead.
```

**What to observe:** Whether the model respects the word limit, clarity of CTA
**Edge Cases:** No product details given
**Failure Modes:** Hallucinates product features, exceeds word limit

---

## Prompt 3
**Technique:** Tone specification

**Prompt:**
```
Write an apology email to a client for a delayed software delivery. Tone: sincere and professional.
```

**What to observe:** Empathy level, whether it offers a resolution
**Edge Cases:** Delay reason not specified
**Failure Modes:** Too robotic, no resolution offered

---

## Prompt 4
**Technique:** Summarisation

**Prompt:**
```
Summarise the following email thread in 3 bullet points, focusing on decisions made and next steps.

[PASTE EMAIL THREAD HERE]
```

**What to observe:** Accuracy, whether it picks up key decisions
**Edge Cases:** Long thread with contradicting statements
**Failure Modes:** Misses key decisions, too vague

---

## Prompt 5
**Technique:** Simple request + constraint

**Prompt:**
```
Write a meeting request email for a 30-minute product demo. Include: purpose, proposed time slot, and a calendar link placeholder.
```

**What to observe:** Structure, whether all 3 elements are included
**Edge Cases:** No timezone given, no recipient name
**Failure Modes:** Vague timing, missing calendar placeholder

---

## Prompt 6
**Technique:** Output format control

**Prompt:**
```
Write 3 subject line options for a re-engagement email to a client who hasn't purchased in 6 months. Return only the 3 subject lines, numbered.
```

**What to observe:** Whether it returns ONLY the subject lines (no extra text)
**Edge Cases:** Ambiguous tone required
**Failure Modes:** Adds unnecessary explanation, all 3 sound the same

---

## Prompt 7
**Technique:** Rewriting

**Prompt:**
```
Rewrite the following email to be 50% shorter without losing the key information.

[PASTE EMAIL HERE]
```

**What to observe:** Compression quality, whether key info is retained
**Edge Cases:** Already short email, email with legal/contractual content
**Failure Modes:** Removes important context, still too long
