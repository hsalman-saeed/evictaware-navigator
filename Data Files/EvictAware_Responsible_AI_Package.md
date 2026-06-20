# EvictAware — Responsible AI Documentation Package
USAII Global AI Hackathon 2026 | Team Vision Forge

---

## SECTION 1: Four-Risk Responsible AI Architecture

### RISK 1 — WRONG STATE LAW APPLIED

**Specific person harmed:** Marcus, a 41-year-old warehouse worker in Houston, Texas, who searches "eviction notice help" at midnight and lands on EvictAware without realizing it's California-specific.

**Exact harm:** Marcus reads a California-based timeline and assumes he has several days of breathing room. He doesn't seek emergency help within Texas's actual, much narrower window, and a default judgment is entered against him before he ever appears in court.

**Probability:** Medium — California's reputation as a strong tenant-protection state means generic searches frequently surface California-specific tools to people in other states.

**Severity:** Critical — the harm is irreversible once the actual jurisdiction's deadline passes.

**Mitigation:** State Scope Lock. At entry, the user must confirm California as their state. If they don't, the app refuses to classify any notice or generate any plan — it outputs only a referral message and a link to find their own state's tenant resources. No California confirmation, no access to any further screen.

**Residual risk:** A user can falsely self-attest California residency to bypass the lock (e.g., someone who recently moved, or is confused about which state's law governs a lease signed elsewhere).

**Devpost language (37 words):** "A State Scope Lock halts the app at entry for any non-California user — no notice classification, no action plan, only a referral out. This prevents a Texas renter from acting on a California-only deadline that doesn't apply to them."

---

### RISK 2 — NOTICE TYPE MISCLASSIFICATION

**Specific person harmed:** Dana, a 34-year-old home health aide in Bakersfield, who received a 3-Day Notice to Quit for a lease violation (no payment option exists) that the AI initially reads as a 3-Day Notice to Pay Rent or Quit.

**Exact harm:** Believing she can cure the notice with money, Dana borrows from family and pays her landlord — a payment that has no legal effect on the actual notice. She wastes her entire 3-day window pursuing the wrong remedy and is evicted anyway.

**Probability:** Medium — self-drafted landlord notices vary in wording and often blur the boundary between curable and non-curable language.

**Severity:** High — direct financial harm plus the loss of the only window she had to respond correctly.

**Mitigation:** Confirmation Gate. The AI shows its classification alongside the specific document language that triggered it (e.g., "Does your notice include a dollar amount and the words 'pay or quit'?") and requires the user to actively confirm a match. Two failed re-classification attempts trigger a manual selection list of all 9+ notice types with example text. The action plan is architecturally incapable of rendering without a recorded confirmation event.

**Residual risk:** A user without the physical notice in hand — lost, torn, or only remembered from a glance — can still confirm an incorrect classification, since the gate verifies user certainty, not document accuracy.

**Devpost language (38 words):** "A Confirmation Gate blocks any action plan until the user verifies the AI's notice classification against checklist language from their real document, with a manual fallback list after two failed attempts — preventing a tenant from pursuing a payment cure that doesn't legally exist."

---

### RISK 3 — OVER-RELIANCE AND MISSED DEFENSE

**Specific person harmed:** Linda, a 67-year-old retired school cafeteria worker in Stockton, whose unit has an unrepaired heater and mold — a habitability defense that could win her case in court.

**Exact harm:** EvictAware's action plan looks complete and authoritative. Linda follows the steps it gives her and never calls legal aid, because the app doesn't surface that her habitability issue could be an independent defense. She misses raising it at her hearing, and a judgment for possession is entered against a case she could have won.

**Probability:** Medium-high — this is the most common failure mode of legal-information tools that present polished, finished-looking output.

**Severity:** Critical — she loses a winnable case.

**Mitigation:** Mandatory Legal Aid Acknowledgment Gate. Before any plan renders, the user must click an active button (not scroll past text) on a statement explaining that EvictAware cannot see their full situation and that a free legal aid review might surface a defense the app can't detect.

**Residual risk:** A user can click through the acknowledgment without absorbing it. The gate guarantees exposure to the message; it cannot guarantee comprehension or that the user actually calls.

**Devpost language (36 words):** "A Mandatory Legal Aid Acknowledgment requires an active click — not a scroll-past — stating the app cannot see a user's full case and a free lawyer might find a defense it can't, before any action plan is allowed to render."

---

### RISK 4 — STRESS-STATE ACCESSIBILITY FAILURE

**Specific person harmed:** Priya Sharma, 29, a part-time medical billing specialist and Uber Eats driver in Fresno, who found her notice taped to the door at 9:47 PM.

**Exact harm:** Research on acute stress and reading comprehension shows people miss embedded deadlines and misjudge urgency under distress. If EvictAware's output is text-dense or buries the deadline mid-paragraph, Priya reads a correct, accurate action plan — and still misses her deadline, not because the information was wrong, but because her cognitive state at that moment couldn't process it as written.

**Probability:** High — the entire user base reaches this app at a moment of acute stress, by design of the problem it solves.

**Severity:** Critical — a missed deadline closes legal options permanently, regardless of how accurate the underlying content was.

**Mitigation:** Stress-State Accessibility Design, enforced by an output validation layer rather than model instruction: Grade 7 reading-level cap, maximum 3 action items per urgency tier, deadlines displayed in isolated [DAY, DATE:] format at the start of each item (never embedded in prose), and a 25-word sentence limit. Output that violates any constraint is rejected and regenerated before it reaches the user.

**Residual risk:** Individual variation in stress response and any additional cognitive or sensory disabilities mean formatting reduces, but cannot fully eliminate, the chance that critical information is missed.

**Devpost language (39 words):** "A validation layer — not model instruction — enforces a Grade 7 reading cap, 3-item tier limits, and isolated [DAY, DATE:] deadline formatting on every output, because a technically correct plan a panicked tenant misreads at 9:47 PM is still a failure."

---

## SECTION 2: Two Human-in-Loop Decisions

### DECISION 1 — ELIGIBILITY DETERMINATION

**The exact boundary:** EvictAware never states that a user qualifies for a legal protection, will win in court, or has a specific defense. It presents what California law generally says for situations like theirs, then routes to a human attorney for case-specific determination.

**Why no AI can make this decision:** Eligibility depends on facts no text description can fully capture — exactly how and when the notice was served, complete lease terms, full payment history, the landlord's prior conduct, and credibility judgments a judge will eventually make. An information tool has no way to verify or weigh any of these.

**Who makes this decision:** A licensed California attorney (State Bar of California) or a certified legal aid advocate who reviews the actual notice, lease, and payment records, and can apply professional judgment under rules of legal responsibility that an AI tool has no standing to exercise.

**Exact on-screen language:** "We can tell you what California law usually says. We can't tell you if it applies to your exact case. A free legal aid lawyer can look at your real papers and tell you that."

**Devpost language (35 words):** "EvictAware never tells a user they qualify for a protection or will win in court — only a licensed attorney reviewing the real notice, lease, and payment history can make that call, and we route every user to one."

---

### DECISION 2 — CASE SEVERITY / HIDDEN RISK FACTORS ("LETHALITY OF LEGAL SITUATION")

**The exact boundary:** EvictAware never assesses whether hidden case factors — an already-issued writ of possession, a prior default judgment, an invalid lease, a habitability defense, VAWA protection — change the real urgency or likely outcome of a case. It routes to a human at every tier instead.

**Why no AI can make this decision:** These factors live in actual court records and case files the app never accesses. Guessing at them from a user's free-text description risks either false reassurance (missing that a case is already further along than it looks) or false panic (assuming the worst when it isn't true) — both of which are worse than admitting the limit.

**Who makes this decision:** A tenant rights attorney or legal aid intake specialist who can pull the real court case file and cross-check county records, something no text-input tool can do.

**Exact on-screen language:** "Some situations are more serious than they look on paper — like a notice that already went to court. We can't check court records. A tenant rights lawyer can, often for free."

**Devpost language (33 words):** "EvictAware can't detect hidden risk factors like an existing court judgment, because that requires checking real court records it never accesses — so every tier routes the user to a tenant rights attorney who can."

---

## SECTION 3: Language Safety Framework

### 3A. The "May" Enforcement System

**Prohibited phrases → required alternatives:**

| Prohibited | Required alternative |
|---|---|
| "You will win" | "Tenants in similar situations may have a stronger case when..." |
| "You qualify for" | "You may be eligible for — confirm with legal aid" |
| "This notice is invalid" | "This notice may have a problem with ___; a lawyer can confirm" |
| "The judge will rule" | "Judges may consider ___ in similar cases" |
| "Your landlord cannot evict you" | "Your landlord may not be able to evict you for this without first ___" |
| "You have until [date], guaranteed" | "Based on what you described, the deadline appears to be [date] — confirm the exact date on your paper notice" |
| "This is illegal" | "This may violate California law under ___; legal aid can confirm" |
| "You don't need a lawyer" | "Legal aid is free and can give you certainty an app cannot" |
| "Definitely" / "certainly" / "guaranteed" | "likely" / "in many cases" / "generally" |
| "This will protect you" | "This step may help protect your rights" |

**Detection mechanism:** Before any output reaches the screen, a validation layer runs pattern matching against this banned-phrase list — string and regex matching for absolute verbs and certainty markers, not a request for the model to "be careful."

**On detection:** A flagged output triggers an automatic re-prompt, returning the specific violating phrase to the model with an instruction to rewrite using the approved uncertainty templates below. If the rewritten output also fails the scan, the system discards both attempts and renders a pre-written, attorney-reviewed cached response for that notice type and scenario instead — guaranteeing the user never sees an unscreened absolute claim.

**Why this matters specifically for legal information:** The harm in a legal-information tool isn't usually wrong facts — it's false certainty. A stressed user treats confident language as authoritative. For an unrepresented tenant, the gap between "may" and "will" is the gap between calling a lawyer to check and not checking at all.

### 3B. The Uncertainty Framing Standard

Six approved templates — the only formats permitted for each assessment type:

1. **Notice type identification:** "Based on what you described, this looks like a [NOTICE TYPE]. This isn't certain — please confirm by checking your paper notice."
2. **Rights statements:** "California law generally gives tenants the right to ___ in situations like this. Your exact rights depend on details only a lawyer can check."
3. **Landlord prohibition statements:** "In most cases, a landlord can't ___ before getting a court order. There may be exceptions depending on your situation."
4. **Rental assistance statements:** "You may be eligible for rental assistance in [COUNTY]. Eligibility rules can change — contact the program directly to confirm."
5. **Local ordinance applicability:** "[CITY] may have extra tenant protection rules beyond state law. We couldn't confirm whether all of them currently apply to your address."
6. **Court outcome statements:** "We can't tell you what a judge will decide. Outcomes depend on the evidence, your landlord's actions, and local court practice."

### 3C. The Data Freshness Protocol

- **Top of every session:** A banner reading "Legal info last checked: [DATE]. Laws can change. This is not legal advice."
- **Every output card:** A persistent footer tag: "As of [DATE] — verify before acting."
- **Mandatory disclaimer (verbatim, 56 words):** "EvictAware gives general information, not legal advice. Laws change. We checked this information as of [DATE], but it may be out of date by the time you read it. This is not a substitute for talking to a lawyer. Always confirm deadlines and rules with a free legal aid lawyer or the court before you act."
- **What users are told to do before acting:** Confirm any deadline or rule with legal aid or the court directly — EvictAware is a starting point, not a final answer.

---

## SECTION 4: Devpost Submission Fields — Final Versions

### FIELD A: Responsible AI Guardrail (under 200 words)

EvictAware is built on four mechanical guardrails, not disclaimers. A State Scope Lock refuses to generate any plan for non-California users — without California confirmation, the system halts before processing begins. A Confirmation Gate blocks the action plan from rendering until the user verifies the AI's notice-type classification against checklist language from their actual document, with a manual selection fallback after two failed attempts — this directly prevents a tenant from pursuing a "pay to cure" remedy on a notice that legally has none. Every output passes through a Language Safety Validation layer that scans for prohibited certainty phrases ("you will win," "this is illegal") before display; flagged text triggers an automatic rewrite, and a second failure loads a pre-written, reviewed cached response instead. Most distinctively, our Stress-State Accessibility Design enforces a Grade 7 reading cap, a 3-item limit per urgency tier, and isolated [DAY, DATE:] deadline formatting — because a correct answer a panicked tenant misreads at 9:47 PM is still a failure. Every session displays the date our legal information was last checked, with a reminder to confirm deadlines with legal aid before acting.

### FIELD B: Human-in-Loop Design (under 150 words)

EvictAware draws a hard line at two decisions no AI should make. Eligibility Determination: the app never states a user qualifies for a protection or will win in court, because that requires reviewing the actual notice, lease, payment history, and landlord conduct — facts no text description can fully capture, and credibility judgments only a licensed attorney can make. Case Severity Assessment: the app cannot detect hidden risk factors like an already-issued writ of possession or a prior default judgment, since these require checking real court records the system never accesses. Both boundaries are enforced through exact, Grade 7 on-screen language — "We can't check court records — a tenant rights lawyer can, often for free" — that routes the user to human legal aid at every tier, every time.

### FIELD C: Data Disclosure (under 150 words)

EvictAware's legal content draws on California Civil Code and Code of Civil Procedure eviction provisions, plus publicly available city and county ordinance text for local overlay rules. County legal aid contact information — phone numbers, hours, and intake links — is sourced from 211.org's public directory. Sample tenant scenarios, notice text, and user personas used in testing and demos are synthetic, written by the team to represent realistic notice language and emotional context without using any real tenant's documents or identifying information. Because eviction law and local ordinances change, we built a data freshness strategy: every legal data point carries a "last checked" date displayed to the user, rather than being presented as permanently current. Before submission, the team cross-checked every statute citation, deadline, and legal aid contact against the primary government or 211.org source using a documented verification checklist.

---

## SECTION 5: Pitch Video — Responsible AI Segment (60 seconds, ~150 words)

AI gets things wrong. So we built EvictAware to fail safely. Our Confirmation Gate means the action plan never renders until the user confirms our notice classification matches their real document — because confusing a curable notice with a non-curable one could cost someone their home.

We also made two decisions on purpose that AI never makes. EvictAware never decides if you qualify for a legal protection — only a licensed attorney reviewing your actual case can do that. And EvictAware never assesses hidden risk factors, like a prior court judgment — only a tenant rights lawyer checking real court records can catch that.

Every screen routes you to free legal aid, every time.

What EvictAware does not do: it does not replace a lawyer, it does not guarantee an outcome, and it never tells a tenant they're safe. It tells them what to check, and who to call, before their clock runs out.

---

## SECTION 6: Judge Q&A Preparation — Responsible AI

**Q1: "What happens if someone uses this app and it gives them wrong legal information and they make a worse decision?"**
Every output passes a Language Safety Validation layer before display — banned certainty phrases trigger a rewrite, and repeated failures load a pre-written, attorney-reviewed cached response. The Confirmation Gate also blocks any plan until the user verifies our classification against their real document. If something still goes wrong, every screen routes to free legal aid.

**Q2: "How do you know your California eviction law data is accurate?"**
We sourced legal text directly from California Civil Code, Code of Civil Procedure, and public city ordinances, then cross-checked every citation and deadline against the primary source using a documented checklist before submission. Every data point also shows a "last checked" date, and we route users to legal aid to confirm before acting.

**Q3: "Could someone become over-reliant on this tool and fail to contact an actual attorney?"**
Yes — which is why a Mandatory Legal Aid Acknowledgment requires an active button click, not a scroll-past, before any plan renders. It tells users the app can't see their full case and a free lawyer might find a defense it missed. Every tier then routes to a specific legal aid phone number, not a directory link.

**Q4: "What about users who aren't fluent in English?"**
Today's build is English-only at a Grade 7 reading level. We know that doesn't solve language access, so every screen routes to county legal aid lines that already offer multilingual intake as the human fallback. Multilingual input is on our roadmap, not yet in this validated build.

**Q5: "How do you handle a situation your app wasn't trained on — like a mobile home eviction or a Section 8 housing eviction?"**
Our manual selection list only covers the 8 validated notice types we built and verified. If a situation — like a mobile home park eviction or Section 8 termination — doesn't match any listed type after two failed attempts, the app stops rather than guessing, and routes directly to legal aid.
