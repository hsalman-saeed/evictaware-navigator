# EvictAware — Complete Problem Canvas & Solution Framing
### USAII Global AI Hackathon 2026 | Challenge Brief 4 | Undergraduate Track
### Team Vision Forge | Build Window: June 14–21, 2026

---

## SECTION 1 — THE ONE-LINE PITCH

**Full Pitch Sentence:**

> "We are building an AI-powered solution that helps a California renter who just received an eviction notice and cannot afford a lawyer so they can identify exactly what type of notice they received, understand what their landlord legally cannot do right now, and take the three most important actions in the next 24 hours — without needing to read legal statutes, call a hotline during business hours, or understand legal vocabulary they were never taught."

**Secondary Pitch (opening hook — 18 words):**

> "Your landlord taped a paper to your door. You have rights. Let us show you exactly what they are."

---

## SECTION 2 — THE USER (Problem Understanding — 20%)

### 2A. USER PROFILE — ONE NAMED PERSON

**Name:** Priya Sharma
**Age:** 29
**Occupation:** Part-time remote medical billing specialist; Uber Eats driver on evenings and weekends
**Location:** Fresno, California
**Household:** Priya, her 7-year-old daughter Maya, and Priya's mother (age 60, limited English proficiency)
**Monthly income:** $2,100 net
**Monthly rent:** $1,350

**Triggering event:** On Tuesday evening at 9:47 PM, Priya found a white envelope taped to her apartment door. Inside was a paper with "3-DAY NOTICE TO PAY RENT OR QUIT" printed across the top. She was $340 short on rent this month after an unexpected car repair. Her landlord, who has been pushing her to vacate the unit so he can renovate it and raise rents, hand-delivered the notice rather than mailing it.

**Exact emotional state:** Priya is terrified. She believes this notice means that in three days, police officers will arrive to physically remove her, her daughter, and her elderly mother. She has already called her sister twice. She has not eaten dinner. Her mother keeps asking what is wrong in Punjabi.

**What she has already tried and failed:**
- Googled "eviction notice California" — found a wall of California Code of Civil Procedure §1161 text she cannot parse.
- Called 211 — was placed on hold, hung up after 12 minutes.
- Texted her landlord asking whether she can pay Friday — no response.

**What she is about to do wrong without EvictAware:** Priya is approximately four minutes away from texting her landlord: *"I'll try to be out by Friday. I just need a little more time to move."* This single text — a voluntary statement of intent to vacate — would surrender her legal right to contest the eviction, assert a cure period, raise habitability or retaliation defenses, and challenge the notice's validity. It would create a written record used against her in any subsequent proceeding. She would pay first and last month's deposit on a new unit she cannot afford, pull Maya from school to begin packing, and leave a home she had the legal right to keep.

---

### 2B. THE MOMENT OF ARRIVAL

It is 10:23 PM on a Tuesday. Priya is sitting at her kitchen table. The eviction notice is unfolded in front of her. Her daughter is asleep in the next room. Her phone screen is open to a Google results page showing California Code of Civil Procedure §1161 — a wall of dense statutory language she cannot parse under normal conditions, let alone at 10 PM in acute distress.

She types "evictaware" into her phone browser after a friend texted her the link. She is holding the notice in her left hand and her phone in her right.

She believes — incorrectly — that she must vacate within three days or be physically removed. She thinks the notice is a court order. She thinks her landlord can be at her door Friday morning with a moving crew. She is wrong on all three counts.

This is the moment EvictAware must reach her.

---

### 2C. SCALE — HOW MANY PEOPLE ARE IN THIS EXACT SITUATION

Priya is not an edge case. She is the statistical center of the eviction crisis.

- **~3.6 million** eviction filings are processed in U.S. courts annually *(Princeton Eviction Lab, 2023)*
- **California courts handle 500,000+ unlawful detainer filings per year** *(California Courts Statistical Report, 2022)*
- **20–35% of renters self-vacate** after receiving an eviction notice — before any court proceedings begin — unnecessarily surrendering their legal right to a hearing *(National Housing Law Project)*
- **Renters have legal representation in only 3–10%** of eviction court proceedings; landlords have representation in **80–90%** of cases *(National Coalition for a Civil Right to Counsel)*
- The representation gap means a renter who appears in court without knowing their rights loses even when valid defenses exist

Every statistic above describes Priya. She is not a rare scenario the system must accommodate. She is the primary user the system is built for.

---

### 2D. WHY EXISTING SOLUTIONS FAIL THIS SPECIFIC USER

**Why HUD.gov fails Priya:** HUD's housing rights pages are organized for policymakers and program administrators — not for someone holding a specific document at 10 PM. The pages describe general programs and protections in categorical terms. They do not identify notice types. They do not generate a time-ordered action plan. They require Priya to already know what questions to ask. A renter who cannot identify whether she received a "3-Day Pay or Quit" versus a "3-Day Quit" cannot self-navigate HUD.gov to find information relevant to her situation — because HUD is organized by program, not by crisis.

**Why Google Search fails Priya:** Searching "3-day eviction notice California" returns a mix of landlord guides, legal aid pages, attorney advertisement sites, and forum threads — none tailored to Priya's specific notice type, location, or timeline. Synthesizing accurate, applicable information from six different sources, under acute psychological stress, at 10 PM, while caring for a sleeping child and an anxious parent, is not a task Priya can complete reliably. Google provides access to information. It does not provide interpretation.

**Why the 211 hotline fails Priya:** 211 connects users to social services, not legal interpretation. In Priya's case, she called, was placed on hold, and hung up after 12 minutes. Even if she had reached someone, 211 operators are trained in resource navigation — not legal analysis of eviction notice types. They can refer her to legal aid, but most legal aid offices are closed at 10 PM. The referral itself requires another queue.

**Why a static eviction rights pamphlet fails Priya:** County court pamphlets and fair housing brochures provide accurate general information about tenant rights — but they do not identify what type of notice Priya received. They do not generate a personalized action plan. They do not tell her what she must do in the next 24 hours, specifically. They are written for a general literate audience, presented at a reading level and density that a person under acute stress cannot process. Priya has already tried reading. Reading static text is not the solution.

**Why a traditional legal aid phone consultation fails Priya:** Legal aid organizations offer free consultations — but intake queues run 3–7 business days at major California providers including Bay Area Legal Aid and Central California Legal Services. Even same-day hotlines operate during business hours. Priya's 3-Day Notice was served Tuesday. Her response window closes Friday. She cannot wait three business days to learn she has rights. The system that is supposed to help her is closed when she needs it most.

---

## SECTION 3 — THE PROBLEM (Problem Understanding — 20%)

### 3A. CORE PROBLEM STATEMENT — For Devpost "Project Description" Field

California renters receiving eviction notices cannot quickly identify what type of notice they received, what legal rights still protect them, or what they must do in the next 24–72 hours — causing tens of thousands to voluntarily leave their homes or miss legal deadlines before ever reaching a courtroom.

*(47 words)*

---

### 3B. THE CASCADE OF WRONG DECISIONS

Without EvictAware, Priya's next 96 hours follow this sequence:

1. **Confusion → Wrong belief:** Priya misreads her 3-Day Notice to Pay Rent or Quit as an order to vacate. She believes police will arrive Friday morning. This belief is false, but nothing in her available environment corrects it.

2. **Wrong belief → Self-incriminating communication:** Priya texts her landlord "I'll be out by Friday, just need a little more time." This voluntary written statement of intent to vacate creates a legal record. It can be presented in any subsequent court proceeding as evidence that she acknowledged the tenancy was ending.

3. **Self-incriminating communication → Unnecessary financial expenditure:** Priya begins securing alternative housing under duress — putting a deposit on a more expensive unit, paying first/last month's rent she cannot afford, forfeiting her current security deposit by leaving without formal proceedings.

4. **Unnecessary expenditure → Failure to appear:** Priya does not appear at any unlawful detainer hearing (if one is filed) because she believes she has already agreed to leave. The court enters a default judgment against her — without ever hearing her side.

5. **Default judgment → Long-term housing instability:** The default judgment appears in Priya's rental history for up to seven years, making it significantly harder to secure future housing. Her daughter's school stability, her mother's living situation, and her own economic mobility are all downstream consequences of a single misunderstood document.

Every step in this cascade is preventable. The cascade starts at Step 1 — a misunderstanding that takes EvictAware 14 minutes to correct.

---

### 3C. WHY THIS PROBLEM CANNOT WAIT

California unlawful detainer law creates a compressed, non-extendable timeline that makes the first 24–72 hours after a notice is served the only window in which Priya's options remain open.

- **Day 0 (Tuesday):** Notice served. The 3-day clock begins the following day.
- **Day 3 (Friday):** Deadline to pay rent in full or vacate. After Friday, the landlord may file an unlawful detainer lawsuit.
- **Day 3+5 (the following Wednesday):** If the landlord files, Priya has exactly **5 calendar days** to file a written response with the court. *(California CCP §1167)*. If she does not respond, the court enters a default judgment automatically — without a hearing.
- **Day 3+20:** If she responds and a trial is set, she has at most **20 days** from filing before the trial date.

The window in which knowing her rights changes her outcome is not a week. It is not three days. It is the **24–72 hours after the notice is found**. That is when she must understand what she is looking at. That is when EvictAware must reach her — not after a legal aid appointment, not after a call back from 211. Now.

For a 30-Day or 60-Day Notice, different but equally compressed timelines apply. For any notice type, the first 24 hours determines whether the renter operates from information or from panic. EvictAware is the only tool available at 10:23 PM on a Tuesday that can change which of those two states Priya is in.

---

## SECTION 4 — WHY AI (AI Reasoning — 30%)

### 4A. THE RULE-BASED ALTERNATIVE AND WHY IT FAILS

A decision tree designed to replicate EvictAware's core notice identification function for California alone would require branches for at minimum: 3-Day Notice to Pay Rent or Quit, 3-Day Notice to Quit (unconditional), 3-Day Notice to Perform Covenant or Quit, 30-Day Notice to Terminate Tenancy (under 1 year), 60-Day Notice to Terminate Tenancy (over 1 year), 90-Day Notice (Section 8 tenants), Notice of Belief of Abandonment, Notice of Entry, and hybrid notices. That is 9 primary branches before accounting for local overlays — Los Angeles Rent Stabilization Ordinance, San Francisco Rent Board just-cause requirements, Berkeley Rent Board protections, statewide AB 1482 just-cause rules — and user-specific conditions including protected class status, disability accommodations, COVID-era protections still in effect in some jurisdictions, and remaining lease term. A decision tree for California alone, built to production accuracy, would require **over 200 branches**.

More critically: when Priya types *"I got a paper that says three days"* — the decision tree cannot process it. The system needs a clean categorical input. Real users describe their notices in fragments under stress: *"something about three days and rent"*, *"a yellow paper my landlord left"*, *"it says I have to leave but I paid most of it."* Natural language understanding is not optional in this system. It is the entire intake layer.

The confirmation step (Stage 1) specifically demonstrates why AI is irreplaceable: the system must read a description written in the user's own words, under stress, possibly incomplete, possibly mixed with emotional context (*"my landlord is threatening me and I don't know what to do"*) — and extract the legal document type from that input. No branching logic can do this. This requires language understanding.

---

### 4B. THE THREE AI CAPABILITIES USED AND WHY EACH IS NON-REPLACEABLE

**AI Capability 1: Natural Language Processing (NLP)**

*What it does in plain language:* NLP allows the AI to read and understand text written in everyday language — including incomplete sentences, emotional phrasing, and informal descriptions — and extract structured meaning from it.

*What it processes in EvictAware:* Priya's free-text description of her notice: *"It says I have three days to pay my rent or leave. The amount it says I owe is $340 and my landlord signed it."* The AI reads this, identifies key signals (three days, pay, or leave, specific amount, landlord signature), and maps them to California's notice taxonomy.

*What breaks if removed:* Without NLP, the system requires users to select their notice type from a pre-built menu. Most renters receiving a first eviction notice do not know what category their notice belongs to. A menu presupposes exactly the knowledge that Priya lacks. Removing NLP makes the tool inaccessible to the exact user who needs it most.

---

**AI Capability 2: Contextual Reasoning across Legal Rules**

*What it does in plain language:* Contextual reasoning allows the AI to apply conditional legal rules to a specific user's situation — not just retrieve information, but determine which rules apply given the specific combination of inputs the user has provided.

*What it processes in EvictAware:* After notice type is identified, the AI applies: (a) base California Civil Code protections for that notice type, (b) whether the user's city or county triggers any local overlay protections such as rent stabilization or just-cause eviction requirements, and (c) whether any indicators in the user's description — references to repair requests, rent increases, harassment — suggest additional protections may apply. This is not information retrieval. It is rule application to a specific fact pattern.

*What breaks if removed:* Without contextual reasoning, the system can only display general tenant rights text — the same text Priya already couldn't use from HUD.gov. The entire value of EvictAware is the application of the right rules to her specific situation, not the display of rules in general. Context is the product.

---

**AI Capability 3: Time-Sensitive Priority Generation**

*What it does in plain language:* Priority generation takes a set of applicable legal actions and ranks them by deadline urgency, consequence severity, and required sequence — producing a time-ordered action list rather than an unordered collection of facts.

*What it processes in EvictAware:* After identifying notice type and applicable rights, and knowing the date the notice was received, the AI generates a sequenced plan: what must happen today, what must happen before the notice period expires, and what must be prepared for if a lawsuit is filed. Actions are ordered by consequence of failure, not alphabetically or by category.

*What breaks if removed:* Without priority generation, the output is a list of rights — accurate but not actionable. Telling Priya *"you have the right to pay within three days"* and *"you have the right to raise habitability defenses"* in an unordered list does not help her understand what to do first when she has 14 minutes of mental bandwidth at 10 PM. Urgency ordering is what transforms information into action.

---

### 4C. AI ARCHITECTURE EXPLANATION — For Devpost (148 words)

EvictAware takes two inputs: (1) the user's plain-language description of the eviction notice they received, and (2) their California city or county. Using natural language processing, the AI identifies the notice type from the user's description — no legal vocabulary required. It then confirms the classification with the user before proceeding. Using contextual reasoning applied to California tenant rights law (California Civil Code and Code of Civil Procedure), the AI determines which legal protections apply to this specific notice type in this specific location. Finally, using priority generation, the AI produces a time-ordered action plan in three urgency tiers: next 24 hours, before your notice expires, and if court papers are filed. The user receives a plain-language action plan — not legal advice — alongside a clear statement of what their landlord legally cannot do right now and local legal aid contacts drawn from public data.

---

### 4D. ALTERNATIVE COMPARISON TABLE

| Feature | EvictAware | Static Website | Google Search | Rule-Based Chatbot |
|---|---|---|---|---|
| Understands ambiguous input ("I got a paper about 3 days") | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Identifies notice type from user's own words | ✅ Yes | ❌ No | ❌ No | ⚠️ Only with exact legal phrasing |
| Confirms classification before acting | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Generates time-ordered action plan | ✅ Yes | ❌ No | ❌ No | ⚠️ Limited, unordered |
| Explains what landlord CANNOT do right now | ✅ Yes | ⚠️ Generic only | ⚠️ Varies by source | ❌ No |
| Applies local overlays (city rent stabilization) | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Calculates user's specific deadline from input date | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Connects to local legal aid (specific contact) | ✅ Yes | ⚠️ Generic link only | ❌ No | ❌ No |
| Available at midnight when panic hits | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| Costs $0 for the user | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

---

## SECTION 5 — SOLUTION DESIGN (Solution Design — 25%)

### 5A. THE COMPLETE USER JOURNEY

**Step 1 — Discovery (10:23 PM):**
Priya receives a text from a friend with a link to EvictAware. She opens it on her phone browser. The entry screen displays: *"Did you receive an eviction notice? Let's find out exactly what it means and what you need to do next."* There is no login screen, no app download, no eligibility form. One button: "Get Started." Priya taps it. She now understands: this tool starts with her, not with paperwork.

**Step 2 — Free-Text Input:**
EvictAware displays a single question: *"In your own words, describe what the notice says."* Below the text box: *"It's okay if you're not sure — just tell us what you see. Example: 'It says I have 3 days to pay or leave.'"* Priya types: *"It says 3 days to pay rent or I have to get out. My landlord wrote the amount I owe, $340, and signed it."* She also selects "Fresno" from a city/county dropdown. She now understands: she does not need legal vocabulary to use this tool.

**Step 3 — Classification and Confirmation (3–5 second processing):**
EvictAware processes her input and displays: *"Based on what you described, this appears to be a **3-Day Notice to Pay Rent or Quit** — the most common type of eviction notice in California. Before we show you your rights and next steps, please confirm your notice matches:"*
- *Contains the exact dollar amount of rent owed*
- *States you must pay OR vacate — not just vacate*
- *Is signed by your landlord or property manager*
- *Does NOT mention lease violations or unauthorized occupants*

*"Does this match your notice?"* — Two buttons: "Yes, this matches" / "No, something is different."

Priya checks her notice against the four points. She taps "Yes, this matches." She now understands: the system verified what it found before telling her what to do. She can trust the output.

**Step 4 — The Bold Statement Card:**
Before any action items, EvictAware displays a high-contrast statement that directly contradicts the false belief driving her toward catastrophic action. Priya reads it. For the first time since finding the notice, she does not believe police are coming tomorrow morning. She scrolls down.

**Step 5 — Tier 1: Next 24 Hours (Red):**
Three action cards appear, each with one action, one reason, and one deadline displayed in bold. Card 1 reads: *"Do NOT text or call your landlord saying you will leave. This can be used against you in court."* Deadline: **TONIGHT.** Priya stops. She realizes she was four minutes from sending exactly that text. She puts her phone down differently now. She now understands: the action she was about to take would have harmed her case.

**Step 6 — Tier 2: Before Your 3 Days Expire (Orange):**
The tier header displays a calculated deadline: *"⏰ Your deadline: **FRIDAY** (3 days start the day after you received the notice. Today is Tuesday.)"* Card 1: *"Contact Central California Legal Services — they offer free tenant consultations. Hours: Monday–Friday 9 AM–5 PM."* Card 2: *"If you can pay the $340, do so by money order, keep the receipt, and send written confirmation to your landlord."* Card 3: *"Know your options if you cannot pay — a legal aid attorney can tell you whether you have defenses that make payment less urgent."* She now understands: she has more time than she thought, and options she did not know existed.

**Step 7 — Tier 3: If Your Landlord Files Court Papers (Yellow):**
Card 1: *"You have exactly 5 days to respond in writing after being served court papers. Missing this deadline means automatic judgment against you."* Card 2: *"Go to the Fresno County courthouse self-help center — they provide free help completing the response form (UD-105)."* Card 3 includes a tap-to-call button: *"Central California Legal Services: (559) XXX-XXXX — Free tenant representation for income-eligible Fresno residents. Online intake: [link]."* Priya screenshots this screen. She now understands: the process does not end if she cannot pay. She has a path forward.

**Step 8 — "What Your Landlord CANNOT Do Right Now" Module:**
A dedicated panel below the tiers displays five items with checkmarks and legal basis:
- ❌ Remove your belongings — requires a court order
- ❌ Change your locks — illegal, Civil Code §789.3
- ❌ Turn off your utilities — illegal
- ❌ Enter your unit without your permission — requires proper notice
- ❌ Threaten or physically pressure you to leave — reportable and illegal

She now understands: she does not have to move this weekend. No one is coming Friday.

**Step 9 — First Action:**
Priya identifies her first concrete action for tomorrow morning: call Central California Legal Services at 9:00 AM. She has a specific phone number. A specific time. A specific purpose. The tool is closed.

**Step 10 — Outcome:**
Priya does not text her landlord tonight. She does not pack. She does not pay a deposit on a new apartment. She calls legal aid Thursday morning, learns she may have a retaliation defense based on her landlord's documented pressure campaign, and is connected with a pro bono attorney. Her case is resolved with a 60-day payment plan. She stays in her apartment. Her daughter does not change schools.

---

### 5B. SYSTEM ARCHITECTURE — PLAIN LANGUAGE VERSION (Demo Narration)

**Stage 1: Notice Identification and Confirmation**
Priya describes her notice in her own words — no legal vocabulary required — and EvictAware's language model reads her description to identify which of California's legally distinct notice types she most likely received. The system does not proceed directly to an action plan. Instead, it displays its classification alongside four specific identifying features and requires Priya to confirm that her document matches before anything else renders. This human verification checkpoint ensures that no misclassification silently drives the wrong plan.

**Stage 2: Legal Context and Rights Loading**
Once the notice type is confirmed, EvictAware applies California tenant rights law — specifically the relevant sections of the California Civil Code and Code of Civil Procedure — alongside local ordinance overlays for Priya's city or county. The system determines what the landlord can and cannot legally do based on this specific notice type and location, and flags any indicators in Priya's description (repair requests, rent increases, landlord pressure) that suggest additional protections may apply.

**Stage 3: Time-Ordered Action Plan Generation**
Using the confirmed notice type, the applicable legal rules, and the date Priya received the notice, EvictAware generates a sequenced action plan in three urgency tiers. Every action item is written in plain language at a Grade 7 reading level. Every deadline is displayed in an isolated, high-contrast element — never embedded in paragraph text. The output also generates a local legal aid connection specific to Priya's county, drawn from 211.org and California State Bar public data.

---

### 5C. THE THREE OUTPUT TIERS — EXACT CONTENT

---

#### THE BOLD STATEMENT CARD (Appears First — Before All Tiers)

> ⚠️ **THIS NOTICE IS NOT AN ORDER TO LEAVE.**
>
> A 3-Day Notice to Pay Rent or Quit means your landlord is giving you the chance to pay what you owe within 3 days — or to give up your tenancy. It is **NOT** an order to move out immediately. It is **NOT** a court order. Police are **NOT** coming Friday.
>
> Your landlord **CANNOT** remove your belongings. **CANNOT** change your locks. **CANNOT** turn off your utilities.
>
> You still have legal rights. Read what they are.

*Legal basis: California CCP §1161; California Civil Code §789.3*

This card directly contradicts the single false belief that causes renters to self-vacate. It appears before any tiers, in the largest text on the screen.

---

#### TIER 1 — NEXT 24 HOURS 🔴 (Red / Urgent)

**Action Card 1:**
**Do NOT communicate your intention to vacate.**
Do not text, call, or email your landlord saying you will leave, need more time to move out, or are looking for a new place. Any such statement creates a written record that can be used against you in court.
**Deadline: TONIGHT**

**Action Card 2:**
**Gather every document related to your tenancy.**
Find your lease, every rent payment receipt, all text messages and emails between you and your landlord, and photographs of your unit's current condition. These are your evidence if this case goes to court.
**Deadline: TONIGHT**

**Action Card 3:**
**Do not allow anyone to enter your unit claiming to remove your belongings.**
Your landlord cannot legally enter your unit to remove your property without a court order and a sheriff. If anyone attempts this, call 911 immediately and document everything. This is called a "self-help eviction" and is illegal in California.
**Deadline: ONGOING**

---

#### TIER 2 — BEFORE YOUR 3 DAYS EXPIRE 🟠 (Orange / Important)

*⏰ Your deadline: **FRIDAY** — 3 days begin the day AFTER the notice was served. Weekends count.*

**Action Card 1:**
**Contact a free legal aid organization today — even for 15 minutes.**
Many eviction notices have errors or are subject to legal defenses — including habitability problems, landlord retaliation, or protected class status — that only an attorney can identify. Central California Legal Services offers free tenant consultations. Call them first thing tomorrow morning.
📞 *[Phone from 211.org public data]* | Hours: Mon–Fri 9 AM–5 PM

**Action Card 2:**
**If you can pay the $340, do so now — in writing, with proof.**
Pay the exact amount stated in the notice using a money order or bank transfer. Keep your receipt. Send your landlord written confirmation that payment has been made. Payment within the notice period legally stops the eviction process.
**Deadline: Before Friday**

**Action Card 3:**
**Know what happens if you cannot pay — you still have options.**
Not being able to pay does not mean you have no rights. A legal aid attorney can tell you whether there are defenses available to you — including habitability issues, retaliatory eviction, or errors in the notice itself — that can be raised in court.
**Deadline: Before Friday**

---

#### TIER 3 — IF YOUR LANDLORD FILES COURT PAPERS 🟡 (Yellow / Be Ready)

**Action Card 1:**
**You have exactly 5 days to respond after being served court papers.**
If your landlord files an unlawful detainer lawsuit and you are served with court papers, you must file a written response within 5 calendar days. If you do not respond, the court will enter an automatic judgment against you — without ever hearing your side. *(California CCP §1167)*
**This is a hard deadline. No extensions.**

**Action Card 2:**
**Go to your courthouse self-help center before your response deadline.**
The Fresno County Courthouse Self-Help Center provides free assistance completing the UD-105 response form. You do not need an attorney to file a response. Filing a response forces a hearing where you can present your case.
📍 *[Address from courts.ca.gov public data]*

**Action Card 3:**
**Central California Legal Services offers free tenant representation for Fresno residents.**
Income-qualified Fresno renters can receive free legal representation in unlawful detainer proceedings. Represented tenants have significantly better outcomes — including settlements, payment plans, and case dismissals.
📞 *[Phone]* | Online intake: *[link from 211.org public data]*

---

### 5D. FOUR FEATURES THAT MAKE JUDGES REMEMBER EVIICTAWARE

**Feature 1: The Confirmation Step**
*What it does:* After the AI identifies the notice type from Priya's description, it displays the classification alongside 4 specific identifying features that should match her document — and requires her to actively confirm before the action plan renders.

*Why it matters to the user:* The California eviction notice taxonomy contains legally distinct documents with nearly identical names. A "3-Day Notice to Quit" (unconditional — no cure available) looks almost identical to a "3-Day Notice to Pay Rent or Quit" (curable). If EvictAware misclassifies an unconditional 3-Day Quit as a Pay or Quit, Priya is told she can cure by payment when she legally cannot. She waits to gather money while her deadline passes. The confirmation step creates a human checkpoint that prevents any misclassification from silently driving a wrong action plan.

*Why competing teams won't build it:* Most competing teams will generate output immediately after user input — faster feels better. Building a deliberate verification pause that slows the system down on purpose requires understanding why accuracy is more valuable than speed in this specific use case. This is a design judgment that demonstrates systems-level thinking, not just implementation speed.

---

**Feature 2: The "What Your Landlord CAN and CANNOT Do Right Now" Module**
*What it does:* After the action plan tiers, a dedicated module displays a clear list of what the landlord is legally permitted to do (file an unlawful detainer lawsuit, serve court papers) versus what they cannot do (enter the unit, remove belongings, change locks, turn off utilities, threaten the tenant).

*Why it matters to the user:* The single greatest source of renter panic after receiving an eviction notice is the belief that immediate physical removal is imminent. This module directly neutralizes that fear with specific legal authority. When Priya sees "Your landlord CANNOT change your locks or remove your belongings without a court order," she does not move out this weekend. This module may prevent more unnecessary self-vacations than any other single element in the system.

*Why competing teams won't build it:* Competing teams will focus on telling users what they should do. They will not think to specifically address what users wrongly fear is about to be done to them. This requires understanding the psychological state of the user, not just the legal content.

---

**Feature 3: The State Scope Lock**
*What it does:* On the entry screen, before any input is accepted, EvictAware displays a single mandatory confirmation: *"EvictAware covers California tenant rights only. Are you a renter in California?"* If the user selects "No," the system displays resources for out-of-state renters and ends the session. No California confirmation — no access to the system.

*Why it matters to the user:* Tenant law is state-specific. What is legally true for a 3-Day Notice in California is different in Texas, New York, or Florida. A system without a scope lock will provide California-specific guidance to out-of-state renters — producing catastrophically wrong action plans. The scope lock is not a product limitation. It is a responsible AI design choice that prevents harm to a user who would not know to distrust California-specific output.

*Why competing teams won't build it:* Competing teams building for "all renters" will not implement a hard scope lock because they perceive it as reducing coverage. EvictAware deliberately chooses accuracy over apparent breadth — a design decision that demonstrates the mature responsible AI thinking judges at this level recognize and reward.

---

**Feature 4: The Local Legal Aid Connector**
*What it does:* Using the user's city/county input, EvictAware surfaces 2–3 local legal aid organizations with specific contact information drawn from 211.org and California State Bar public data. Each listing includes: organization name, services, income eligibility threshold, hours of operation, phone number, and online intake link.

*Why it matters to the user:* An action plan that says "contact legal aid" without providing a specific phone number fails. Priya will not independently research which organization to call at 10 PM in a state of panic. The connector transforms a general instruction into a specific, immediately actionable next step. It also reflects the real-world constraint that legal aid organizations have intake requirements and limited hours — by surfacing the right contact for Priya's county, EvictAware maximizes the probability she actually reaches someone when it matters.

*Why competing teams won't build it:* Surfacing accurate, location-specific legal aid contacts requires pulling from real public data sources and treating that connection as part of the product — not a footer. Most competing teams will link to a generic "find legal aid" page or skip it entirely. EvictAware builds the connection into the output, because the connection is the action.

---

## SECTION 6 — RESPONSIBLE AI (Enhanced — 10% + Credibility Multiplier)

### RISK 1 — WRONG STATE LAW APPLIED

**Specific person harmed:** Marco, a renter in El Paso, Texas, finds EvictAware via Google search and does not notice or understand the California-specific scope of the tool. He enters his notice description. EvictAware provides a California-specific action plan — including cure rights under California CCP §1161 that do not apply in Texas. Marco follows the California action plan, believes he has cure rights that Texas law does not guarantee under his specific notice type, misses his actual Texas legal response window, and loses the ability to contest the eviction. He vacates under a misapprehension of the law.

**Mitigation (mechanical — not advisory):**
The State Scope Lock is a hard architectural stop built into the UI routing layer — not a disclaimer appended to output. On application load, before the input field renders, EvictAware displays a single mandatory screen:

*"EvictAware covers California tenant rights only. Tenant laws vary significantly by state, and using California-specific guidance in another state could give you incorrect information. Are you a renter in California?"*

Two buttons: "Yes, I'm in California" / "No, I'm in another state."

If the user selects "No," the system displays resources for out-of-state renters and ends the session. **The notice description input field does not render until California selection is confirmed.** This is enforced at the route level — there is no application path that bypasses this gate. It is not a warning. It is an architectural stop.

---

### RISK 2 — NOTICE TYPE MISCLASSIFICATION

**Specific person harmed:** Daria is a renter in Sacramento who received a "3-Day Notice to Quit" — an unconditional notice issued after a material lease violation (unauthorized subletting). This notice does not offer a cure period. EvictAware, reading Daria's description — *"3-day notice about a problem with the lease"* — misclassifies it as a "3-Day Notice to Pay Rent or Quit" (curable). Daria's action plan tells her to pay the amount owed within three days. There is no amount to pay — the notice is unconditional. Daria spends two days attempting to gather money she cannot pay, misses her deadline to seek legal aid about an actual defense available to her (the subletting arrangement may have been implicitly permitted), and arrives in court without representation and without the correct understanding of her notice type.

**Mitigation (mechanical — The Confirmation Step):**
After classification, EvictAware **does not render the action plan.** Instead, it displays the classified notice type alongside 4 specific identifying features the user must verify against their document, and presents two buttons: "Yes, this matches" / "No, something is different."

The action plan is **architecturally blocked** — it does not render until a positive confirmation is received. If the user selects "No, something is different," the system re-prompts: *"Tell us more about what doesn't match"* and re-classifies based on additional input.

This means: any misclassification that reaches the confirmation step will be caught by the user themselves — because the specific identifying features displayed will not match what they see on their document. The confirmation gate is a mandatory UI step. The plan does not exist until confirmation is given.

---

### RISK 3 — OVER-RELIANCE AND SUBSTITUTION

**Specific person harmed:** Rosa, a renter in Los Angeles, received a 3-Day Notice to Quit after her landlord discovered she had a dog in a no-pet building. Unknown to Rosa, her landlord raised her rent 25% three months ago without complying with Los Angeles's Rent Stabilization Ordinance — a potentially void action. She also has a habitability claim: her bathroom ceiling has been leaking for four months without repair. Under California Civil Code §1942.5, a landlord who retaliates against a tenant for asserting habitability rights cannot legally enforce an eviction notice for 180 days.

If Rosa contacts legal aid, she has strong potential defenses. But EvictAware's action plan is specific, sequenced, and sounds comprehensive. Rosa reads it, feels informed, and decides she understands her situation well enough without calling legal aid. She goes to court unrepresented, does not know how to raise a habitability or retaliation defense, and loses a case she could have won.

**Mitigation (mechanical — Mandatory Legal Aid Acknowledgment):**
Before the action plan renders — above the Bold Statement Card, as the first interactive element in the output — the user encounters a mandatory acknowledgment they must actively dismiss:

> **⚠️ BEFORE YOU READ YOUR PLAN — READ THIS FIRST**
>
> EvictAware gives you a starting point. It is NOT a complete legal picture.
>
> Your situation may include legal defenses that only an attorney can identify — including habitability problems, landlord retaliation, errors in your notice, or protected status under local law. EvictAware cannot assess these.
>
> **This plan does NOT replace legal advice.**
>
> Tapping "I understand — show me my plan" means you understand that contacting a tenant rights attorney or legal aid organization is the most important step you can take.
>
> **[I understand — show me my plan]**

This is not a footer. It is not fine print. It is the **first interactive element** in the output sequence, rendered before the Bold Statement Card. The action plan does not exist until the user actively taps the acknowledgment. Rosa must read and dismiss this before she sees anything else.

---

### RISK 4 — STRESS-STATE ACCESSIBILITY FAILURE

**Specific harm:** Priya correctly reads her Tier 1 action card, but the deadline attached to her Tier 3 response obligation — "You must respond within 5 days of being served" — is embedded in the third sentence of a paragraph-length card. Under acute psychological stress, Priya reads the first sentence and absorbs the action but not the specific number of days. She believes she has "a few days" and misses the 5-calendar-day response deadline after the landlord files. The court enters automatic judgment against her.

This risk is unique because it is not caused by incorrect information — it is caused by accurate information presented in a format that a stressed human brain cannot reliably absorb. Designing for stressed users is not a UX nicety. It is a core safety requirement.

**Mitigation (design-level, mechanical):**

EvictAware enforces the following output constraints at the system prompt level, validated before rendering:

- **Maximum reading level: Grade 7.** All output is generated with explicit system prompt instructions to use plain language at or below 7th-grade reading level. No legal term may appear without an immediate plain-language parenthetical.

- **Deadline display — isolated, never embedded.** Every deadline appears in its own UI element: a box with a colored border and the format **[NUMBER] DAYS — [SPECIFIC DATE] — [ACTION REQUIRED].** Deadlines embedded in paragraph text trigger an output rejection and regeneration.

- **Maximum 3 action items per tier.** The system prompt explicitly limits each tier to 3 cards. Items above this threshold are either consolidated or moved to a secondary "Additional Context" section that does not appear by default.

- **Each card: one action, one reason, one deadline.** Multi-action cards are prohibited in the system prompt. If the AI generates a card with more than one action, the formatting validation layer splits it or flags it for the fallback template.

- **Pre-render validation:** Output text is processed through a formatting check before display. If a deadline appears inside a paragraph rather than in a standalone deadline element, the card is rejected, the constraint violation is logged, and the card is regenerated with correct structure before the user sees it.

---

### HUMAN-IN-LOOP DECISION 1

**The exact decision EvictAware's AI does NOT make:** Whether the user's specific situation constitutes a valid legal defense in a California unlawful detainer proceeding.

**What information would be required:** Assessing a legal defense requires reviewing the original lease, all landlord-tenant communications in chronological order, complete payment history, photographs of the unit's condition, the precise wording of the notice, applicable local ordinance provisions, and the legal relationship between the renter's specific fact pattern and current case law. It requires legal training, professional judgment, ethical obligation to the client, and licensing by the State Bar of California — none of which an AI system possesses or can replicate.

**Who makes this decision:** A licensed California tenant rights attorney or trained legal aid advocate.

**Exact on-screen language:**
> *"EvictAware has shown you your rights and your next steps. It has NOT assessed whether you have a legal defense to this eviction. Defenses like habitability, retaliation, improper notice, or protected class status can only be evaluated by a licensed attorney who reviews your complete situation. Do not assume you do not have a defense. Call the legal aid organization listed below before your deadline."*

---

### HUMAN-IN-LOOP DECISION 2

**The exact decision EvictAware's AI does NOT make:** Whether the eviction notice itself is legally valid and properly served under California law.

**What information would be required:** Notice validity requires assessing the exact method of service (personal delivery, substituted service, or posting-and-mailing), whether the person who served the notice was legally authorized to do so, whether the notice contains all required elements under California CCP §1161 (exact rent amount, period covered, landlord name and address, clear statement of pay-or-quit options), and whether local ordinances impose additional requirements beyond state law. This is a technical legal determination that requires document review by someone trained in California unlawful detainer procedure.

**Who makes this decision:** A licensed California tenant rights attorney or courthouse self-help center staff.

**Exact on-screen language:**
> *"EvictAware cannot tell you whether this notice was served correctly or whether it contains all legally required elements. An improperly served or legally defective notice can be challenged in court — but only if an attorney or self-help center reviews it first. This review takes 15 minutes and is free at most legal aid organizations. It could change everything."*

---

### THE "MAY QUALIFY" FRAMING — HOUSING VERSION

**Prohibited phrases (enforced in system prompt — verbatim list):**
The system prompt explicitly prohibits the AI from generating the following phrases or their functional equivalents:
- "You are legally protected from..."
- "Your landlord cannot evict you"
- "You will win"
- "This eviction is illegal"
- "You qualify for [protection]"
- "You are guaranteed [outcome]"
- "California law protects you from this"
- Any declarative statement of the form "[Subject] cannot [action]" without a preceding uncertainty qualifier

**Output validation (code-level enforcement):**
Before the action plan renders, output text is scanned against a prohibited phrase pattern list. If a prohibited phrase is detected, the output triggers an automatic regeneration request with the instruction: *"Rephrase using required uncertainty framing before displaying."* Output does not render to the user until it clears the validation pass.

**Required uncertainty framing — mandatory templates for all legal assessments:**
All legal assessments in the output use one of the following sentence starters (built into the output template as mandatory fields, not optional language choices):
- *"Based on what you described, it appears that..."*
- *"California law generally provides that in situations like this..."*
- *"Most California tenants in this situation have the right to..."*
- *"It may be the case that..."*
- *"An attorney reviewing your specific situation could confirm whether..."*

Legal assessments are structurally incapable of appearing without one of these templates preceding them. They are output template fields — not stylistic suggestions.

---

## SECTION 7 — IMPACT & INSIGHT (15%)

### 7A. THE IMPACT STATEMENT — BEFORE AND AFTER

**Without EvictAware:**
At 10:23 PM, Priya finds the notice and spends 40 minutes on Google reading legal statutes she cannot parse. She calls 211, waits 12 minutes on hold, and hangs up. At 11:15 PM, she sends her landlord: *"I'll try to be out by Friday."* She spends the next two days in a state of panic — asking her mother whether they can stay with relatives, looking up moving truck prices, pulling Maya from after-school care to begin packing. By Thursday, she has communicated her intent to vacate in writing to both her landlord and her building manager. She vacates Friday.

She was never told she could have paid $340 and stopped the process. She was never told her landlord could not have touched her belongings this week. She is now unhoused with a 7-year-old and an elderly parent. No unlawful detainer proceeding was ever filed. Her case never entered the court system. She simply disappeared from her home. Her story is invisible in the data — she is counted as a voluntary departure, not an eviction.

**With EvictAware:**
At 10:23 PM, Priya opens EvictAware. By 10:37 PM — fourteen minutes later — she knows: her notice is a 3-Day Pay or Quit, not an order to leave. Her landlord cannot touch her belongings, change her locks, or enter her unit without a court order this weekend. She has until Friday to pay or begin contesting. She should not contact her landlord tonight. She should call Central California Legal Services at 9 AM tomorrow.

She does not send the text. She does not pack. She calls legal aid Thursday morning, learns she may have a retaliation defense based on her landlord's documented pressure campaign, and is connected with a volunteer attorney. Her case resolves with a 60-day payment plan. She stays in her apartment. Maya stays in her school. Her mother stays in her home.

Fourteen minutes. One clear action plan. One phone number for tomorrow morning. One family that stays housed.

---

### 7B. THE QUANTIFIED SCALE OF IMPACT

- California courts process approximately **500,000+ unlawful detainer filings annually** *(California Courts Statistical Report, 2022)*
- Approximately **40% of eviction cases nationally result in default judgment** — the renter never appeared or responded *(Princeton Eviction Lab, 2023)*
- An estimated **20–35% of renters self-vacate** after receiving a notice — before the case ever reaches court *(National Housing Law Project)*
- Renters have legal representation in only **3–10% of eviction proceedings**; landlords have representation in **80–90%** of cases *(National Coalition for a Civil Right to Counsel)*
- The average economic cost of an eviction to a renter — including moving costs, lost deposits, temporary housing, and income disruption — is estimated at **$7,000–$9,000** *(Urban Institute, 2021)*
- If EvictAware reaches even 5% of California's self-vacating renters and helps half of them make a better-informed decision, the system could positively influence outcomes for approximately **5,000–12,500 California renters annually**

---

### 7C. THE FRICTION REDUCTION STATEMENT — For Devpost (47 words)

EvictAware removes the friction that turns a correctable situation into an irreversible one: the gap between a renter receiving a notice and understanding what it means. By transforming confusion — *"I don't know what this paper means"* — into clarity — *"This is a 3-Day Pay or Quit and here is what I can do"* — and clarity into action — *"Here are my three next steps and the phone number to call tomorrow"* — EvictAware gives the most time-constrained users the one thing they need most: enough understanding to make the right decision in the next 24 hours.

---

### 7D. BEYOND PRIYA — THE POPULATION THIS SERVES

**First-time eviction notice recipients** — who have never encountered this document and have no framework for interpreting it. EvictAware's plain-language output is explicitly written for someone who has never heard the phrase "unlawful detainer" before today.

**Non-native English speakers** — for whom legal English is doubly inaccessible. EvictAware's Grade 7 reading level and jargon-free output dramatically lower the language barrier. A Spanish-language version (CCP §1161 is the same law in both languages) is the immediate next-priority expansion path.

**Renters without internet literacy** — who struggle to navigate multi-page information architectures. EvictAware's single free-text entry point and linear output flow eliminate the need to navigate, compare sources, or synthesize information from multiple documents. One input. One output. One path through.

**Renters with disabilities** — including cognitive processing differences, visual impairments, or anxiety disorders that impair reading comprehension under stress. The output constraints — maximum 3 items per tier, isolated deadline display, plain language, high contrast — are specifically designed to be accessible without requiring assistive technology configuration.

**Renters who work multiple jobs** — like Priya, who cannot call legal aid during business hours and cannot wait three days for an appointment. EvictAware is available at 10:23 PM Tuesday because that is when the notice is found. No appointment. No hold time. No eligibility screening to access information.

**Community case managers and housing navigators** — who work with multiple housing-unstable clients simultaneously. EvictAware can serve as a rapid orientation tool: a navigator enters a client's notice description in a 5-minute intake and generates an action plan that prepares the client for their first legal aid consultation, arriving informed rather than in crisis.

---

## SECTION 8 — DATA PLAN

### 8A. PUBLIC DATA SOURCES

**1. California Courts Self-Help — Eviction (Landlord-Tenant)**
URL: https://www.courts.ca.gov/selfhelp-eviction.htm
*Information taken:* Notice type definitions, unlawful detainer filing procedures, response deadlines (5 calendar days), hearing timelines, UD-105 response form guidance, courthouse self-help center directory
*How used:* Core content for Stage 2 (Legal Context Loading) and Stage 3 (Action Plan Generation); Tier 2 and Tier 3 action items; self-help center referrals

**2. California Civil Code — Sections 1940–1954.06**
URL: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml
*Key sections:* §1942 (implied warranty of habitability), §1942.5 (retaliatory eviction prohibition — 180-day protection), §789.3 (self-help eviction prohibition and tenant remedies), §1950.5 (security deposit rights and return timelines)
*How used:* Legal basis for the "What Your Landlord CANNOT Do Right Now" module; retaliation and habitability flag triggers in the Human-in-Loop prompts

**3. California Code of Civil Procedure — Sections 1161–1179.06**
URL: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml
*Key sections:* §1161 (grounds for unlawful detainer and notice requirements), §1161.1 (pay or quit notice requirements — exact amount required), §1167 (5-day response period after service), §1179 (court discretion to grant relief from forfeiture)
*How used:* Notice type classification logic; deadline calculation; Tier 1, 2, and 3 action item legal basis; response deadline warnings

**4. HUD Emergency Rental Assistance Programs**
URL: https://www.hud.gov/program_offices/comm_planning/rental-assistance
*Information taken:* Federal rental assistance program availability by state, program eligibility thresholds, California ERA program finder
*How used:* Tier 2 financial assistance options for users who indicate inability to pay full rent amount

**5. 211.org — California Tenant Services Directory**
URL: https://www.211.org
*Information taken:* Legal aid organization listings by California county, housing services, tenant rights hotlines with hours and contact information
*How used:* Local Legal Aid Connector — populates county-specific contact information in Tier 3 based on user's city/county input

**6. California State Bar — Legal Aid and Pro Bono Services Directory**
URL: https://www.calbar.ca.gov/Public/Need-Legal-Help/Legal-Aid-and-Pro-Bono-Services
*Information taken:* Legal aid organization directory by county, income eligibility thresholds, free consultation availability
*How used:* Supplemental source and cross-validation for Local Legal Aid Connector listings

**7. City-Specific Local Ordinance Sources:**
- Los Angeles Housing Department — Tenant Protections: https://housing.lacity.gov/residents/tenant-protections (LARSO, just-cause eviction, relocation assistance)
- San Francisco Rent Board: https://sfrb.org (just-cause requirements, RSO protections)
- Berkeley Rent Stabilization Board: https://www.cityofberkeley.info/rent/ (just-cause eviction, rent increase limits)
*How used:* Stage 2 local overlay logic — when user identifies their city, system checks for city-specific protections that apply beyond state law baseline

---

### 8B. SYNTHETIC DATA PLAN

**Synthetic User Scenarios — 20 total, generated with GPT-4:**

Generation method: Each scenario was generated using the prompt structure: *"Generate a realistic scenario for a California renter receiving the following notice type, with the following complicating factors. Include the user's description of the notice in their own words, their household situation, and two details they mention that might indicate additional legal protections or risks."*

Scenario coverage:
- 3-Day Notice to Pay Rent or Quit (standard) — 3 scenarios
- 3-Day Notice to Pay Rent or Quit (partial payment available) — 2 scenarios
- 3-Day Notice to Quit (unconditional, lease violation) — 3 scenarios
- 3-Day Notice to Perform Covenant or Quit — 2 scenarios
- 30-Day Notice to Terminate Tenancy (under 1 year) — 2 scenarios
- 60-Day Notice to Terminate Tenancy (over 1 year) — 2 scenarios
- Notice with habitability defense indicator — 2 scenarios
- Notice with retaliation indicator — 2 scenarios
- Notice from out-of-state user (scope lock test case) — 2 scenarios

**Test Case Library:**
All 20 scenarios are run through EvictAware's full pipeline to verify: correct notice type classification, accurate confirmation step display, correct tier content for that notice type, correct deadline calculation from input date, and appropriate legal aid connector output for the specified county.

**Demo Scenario Data:**
The demo uses Priya's scenario verbatim: *"I got a paper taped to my door tonight. It says I have 3 days to pay my rent or I have to leave. The amount it says I owe is $340. My landlord signed it. I'm in Fresno, California."* This input is pre-loaded in the demo environment and produces the complete output flow shown to judges.

---

### 8C. DATA FRESHNESS AND ACCURACY STRATEGY

**Version Date Display:**
Every output screen includes a persistent, visible footer: *"EvictAware legal content last reviewed: [Month Year]. California tenant law may change. Verify information before acting."*

**Specific Disclaimer Language (verbatim, appears on every output screen):**
> *"This information is based on publicly available California court guidance and state law as of [date]. Laws and local ordinances may have changed since this content was last reviewed. Before taking any legal action based on this plan, confirm current rules with a legal aid organization or visit courts.ca.gov for the most current information."*

**User Instructions Before Acting:**
Every action item in Tier 2 and Tier 3 that references a specific legal right includes: *"Confirm this applies to your situation by calling [legal aid contact] or visiting courts.ca.gov before acting on this step."*

**Production Maintenance Protocol (designed and disclosed, not yet built in MVP):**
In a production version, EvictAware would implement:
- **Quarterly human review cycle:** A licensed California tenant rights attorney or qualified law student volunteer reviews all legal content against current California law every 90 days.
- **Legislative change monitoring:** The system monitors California Legislature update feeds (leginfo.legislature.ca.gov) for amendments to CCP §1161 and relevant Civil Code sections.
- **Version stamping with staleness warning:** Content older than 90 days triggers an enhanced warning prompting users to verify currency before acting.
- **The MVP uses a static JSON file for legal content.** The version date and disclaimer are manually updated. This limitation is explicitly acknowledged in the submission. The maintenance gap is disclosed, not hidden.

---

## SECTION 9 — ORGANIZATION INSPIRATION

### Organization 1: Code for America

**What they do:** Code for America builds technology products with and for government agencies and social service organizations, making public systems more accessible and human-centered for the people who depend on them most.

**How EvictAware reflects their approach:** Code for America's core principle is that technology should serve people who need government systems most — not the systems themselves. GetCalFresh demonstrates that an AI-assisted conversational interface can dramatically increase the rate at which eligible people actually access benefits they are already entitled to. EvictAware applies this exact principle to tenant rights: it does not create new legal rights, it makes existing rights findable and usable for someone in crisis at 10 PM who would otherwise navigate alone and fail.

**Specific design decision inspired by Code for America:** EvictAware's single-question free-text entry point — *"Describe your notice in your own words"* — is directly inspired by GetCalFresh's design choice to start where the user is, in their own language, rather than requiring them to navigate a system built for administrators. Like GetCalFresh, EvictAware begins with what the user knows rather than what the system needs.

---

### Organization 2: Benefits Data Trust (BDT)

**What they do:** Benefits Data Trust uses data, technology, and policy advocacy to connect people to public benefits they are eligible for but not receiving — focusing specifically on reducing the friction between eligibility and enrollment.

**How EvictAware reflects their approach:** BDT's foundational insight is that the largest barrier to public benefit access is not eligibility — it is navigation. People who qualify for SNAP, Medicaid, and utility assistance are not receiving it because the process of confirming eligibility and completing enrollment is too complex, too time-consuming, and too dependent on institutional knowledge. EvictAware applies this same insight to tenant rights: Priya's barrier is not that she lacks rights. It is that she cannot understand them, navigate toward them, or act on them in a moment of crisis without support.

**Specific design decision inspired by BDT:** EvictAware's Local Legal Aid Connector — which surfaces a specific phone number and intake link rather than a link to a general "find help" directory — is directly inspired by BDT's finding that providing a direct phone number (rather than a website) significantly increases the rate at which people in need actually reach help. EvictAware treats the connection itself as a product deliverable, not a footer.

---

## SECTION 10 — DEVPOST SUBMISSION FIELDS (DRAFT)

### FIELD: Project Description

California renters receiving eviction notices face a system designed against them. Every year, hundreds of thousands of California renters receive eviction notices they cannot understand — not because they are uninformed, but because eviction law is complex, notice types are legally distinct in consequential ways, and the window for action is 24–72 hours. Research shows that 20–35% of renters self-vacate after receiving a notice, surrendering legal rights they never knew they had.

EvictAware is an AI-powered California Tenant Rights Navigator designed for the person holding an eviction notice at 10 PM with no lawyer, no time, and no framework for understanding what they are looking at. Using natural language processing, EvictAware reads the user's plain-language description of their notice, identifies the notice type, confirms that classification with the user, and generates a time-ordered action plan in three urgency tiers: what to do in the next 24 hours, what must happen before the notice period expires, and what to prepare for if court papers are filed.

EvictAware does not provide legal advice. It provides legal orientation — the critical first layer of understanding that allows a person to stop panicking, understand their immediate rights, and take the right next step before their window of action closes.

Our user is Priya — 29, Fresno, California, medical billing specialist and single mother. At 10:23 PM on a Tuesday, she found a 3-Day Notice to Pay Rent or Quit taped to her door. Without EvictAware, she would have texted her landlord "I'll be out Friday" — voluntarily vacating a home she had the right to keep. With EvictAware, fourteen minutes later, she knows what her notice means, what her landlord cannot do this weekend, and exactly who to call tomorrow morning.

---

### FIELD: AI Architecture Explanation *(148 words — use verbatim)*

EvictAware takes two inputs: (1) the user's plain-language description of the eviction notice they received, and (2) their California city or county. Using natural language processing, the AI identifies the notice type from the user's description — no legal vocabulary required. It then confirms the classification with the user before proceeding. Using contextual reasoning applied to California tenant rights law (California Civil Code and Code of Civil Procedure), the AI determines which legal protections apply to this specific notice type in this specific location. Finally, using priority generation, the AI produces a time-ordered action plan in three urgency tiers: next 24 hours, before your notice expires, and if court papers are filed. The user receives a plain-language action plan — not legal advice — alongside a clear statement of what their landlord legally cannot do right now and local legal aid contacts drawn from public data.

---

### FIELD: Human-in-Loop Design

EvictAware's AI does not make two decisions — and is explicitly designed not to.

**Decision 1:** Whether the user's situation constitutes a valid legal defense in an unlawful detainer proceeding. Assessing a legal defense requires reviewing the original lease, all landlord-tenant communications, payment history, and applying professional legal judgment — capabilities AI cannot provide. This decision belongs to a licensed California tenant rights attorney. Every output screen states: *"EvictAware has not assessed whether you have a legal defense. Defenses can only be identified by an attorney. Contact the legal aid organization listed before your deadline."*

**Decision 2:** Whether the eviction notice is legally valid and properly served under California law. Notice validity requires assessing service method, required content elements, and local ordinance compliance. EvictAware explicitly states: *"EvictAware cannot tell you if this notice was served correctly. An attorney can review your notice for free. An improperly served notice can be challenged in court."*

---

### FIELD: Responsible AI Guardrail

**Risk:** Notice type misclassification. California has legally distinct eviction notice types that produce completely different action plans. A 3-Day Pay or Quit (curable by payment) and a 3-Day Quit (unconditional — no cure available) look similar but require entirely different responses. If EvictAware misclassifies a 3-Day Quit as a Pay or Quit, a renter is told they can resolve the issue by paying when they legally cannot — causing them to miss their actual legal response window while gathering money they cannot use.

**Mitigation (architectural):** After classification, EvictAware does not render the action plan. Instead, it displays the classified notice type alongside 4 specific identifying features and presents a mandatory confirmation gate: the user must actively confirm that these features match their document before the plan renders. The action plan is architecturally blocked until confirmation is received. Any misclassification is caught by the user themselves before it drives a single wrong action.

---

### FIELD: Data Disclosure

EvictAware uses exclusively public data. No private or personal data was used in development or testing.

**Legal content sources:**
- California Courts Self-Help Eviction guidance (courts.ca.gov)
- California Civil Code §§1940–1954.06 — habitability, retaliation, self-help eviction (leginfo.legislature.ca.gov)
- California Code of Civil Procedure §§1161–1179.06 — notice requirements, unlawful detainer procedure, response deadlines (leginfo.legislature.ca.gov)
- HUD Emergency Rental Assistance Programs (hud.gov)
- 211.org California tenant services and legal aid directory
- California State Bar Legal Aid and Pro Bono directory (calbar.ca.gov)
- City-specific ordinances: Los Angeles (housing.lacity.gov), San Francisco (sfrb.org), Berkeley (cityofberkeley.info/rent)

**Synthetic data:** 20 synthetic user scenarios generated using GPT-4 for system testing and demo purposes. Scenarios cover 8 distinct California notice types, edge cases including habitability and retaliation indicators, and out-of-state scope lock test cases. No real user data was used.

**Data freshness:** All legal content is date-stamped. Users are explicitly instructed to verify current law before acting. The MVP uses a static JSON legal content file; production maintenance would require quarterly attorney review.

**AI tools used:** [Team to complete — Claude API for conversational AI, GPT-4 for synthetic scenario generation, additional tools as used]

---

## SECTION 11 — THE WOW MOMENT (Demo Anchor)

The demo is 45 seconds. Here is exactly what happens.

**The setup:**
The narrator says: *"It's 10:23 PM on a Tuesday. Priya just found this taped to her apartment door."* The screen shows the notice — "3-DAY NOTICE TO PAY RENT OR QUIT" at the top, $340 amount, landlord signature. The narrator continues: *"She thinks she has three days to leave. She's four minutes away from texting her landlord 'I'll be out Friday.' Let's see what happens when she opens EvictAware instead."*

---

**What the user types:**
> *"I got a paper on my door tonight. It says 3 days to pay my rent or I have to leave. It has the amount I owe, $340, and my landlord signed it. I'm in Fresno, California."*

Three-second processing pause.

---

**What appears on screen first — THE BOLD STATEMENT CARD:**

On a dark background, in large high-contrast text:

> ⚠️ **THIS NOTICE IS NOT AN ORDER TO LEAVE.**
>
> A 3-Day Notice to Pay Rent or Quit gives you **3 days to pay what you owe** — or to give up your tenancy. It is **NOT** a court order. Police are **NOT** coming Friday.
>
> Your landlord **CANNOT** remove your belongings. **CANNOT** change your locks. **CANNOT** turn off your utilities. **You still have legal rights. Read what they are.**

---

**What the countdown tiers show:**

🔴 **NEXT 24 HOURS — 3 Actions**
- Card 1: *"Do NOT text your landlord saying you'll leave."* — **Deadline: TONIGHT**
- Card 2: *"Gather your lease, receipts, and landlord texts."* — **Deadline: TONIGHT**
- Card 3: *"Do not let anyone into your unit without your permission."* — **Deadline: ONGOING**

🟠 **BEFORE YOUR 3 DAYS EXPIRE**
⏰ *Your deadline: **FRIDAY** (3 days begin the day after service. Today is Tuesday.)*
- Card 1: *"Call Central California Legal Services tomorrow at 9 AM — free tenant consultations."* 📞 [specific number]
- Card 2: *"If you can pay $340, do it by money order. Keep your receipt."*
- Card 3: *"Not being able to pay does not mean you have no options."*

**The "What Your Landlord CANNOT Do Right Now" module:**

> ❌ Remove your belongings — requires a court order
> ❌ Change your locks — illegal, Civil Code §789.3
> ❌ Turn off utilities — illegal
> ❌ Enter without notice — illegal
> ❌ Threaten or pressure you — reportable and illegal

---

**Why this moment is impossible to replicate with any other tool:**

A static website cannot take *"3 days to pay my rent or I have to leave, $340, Fresno"* and respond in 5 seconds with a specific notice type identification, a calculated Friday deadline, a specific legal aid phone number, and a list of what her landlord cannot do this weekend. Google cannot. A rule-based chatbot requires Priya to already know the legal name of her notice type. A pamphlet cannot calculate a Friday deadline from a Tuesday service date and surface the specific Fresno legal aid office hours. Only EvictAware does all of this from a single free-text input.

---

**The emotional arc of the demo:**

🚨 **Panic** — *"Police are coming Friday. I have to leave. I'm going to text my landlord right now."*
↓
📄 **Clarity** — *"This is a 3-Day Pay or Quit. This is what it means."*
↓
💪 **Confidence** — *"My landlord cannot touch my belongings this weekend. I have rights."*
↓
✅ **Action** — *"I'm calling Central California Legal Services at 9 AM tomorrow. I have the number."*

The demo ends here. The judge has watched a real person arrive in a moment of panic and leave with a specific plan, a specific phone number, and a specific time to call. In under two minutes. That is the product.

---

## SECTION 12 — THE COMPETITIVE DIFFERENTIATION STATEMENT

**Statement 1:**
*"Other teams will build a resource directory that lists California tenant rights programs. EvictAware builds a notice interpreter instead — because knowing that tenant protections exist is not the same as understanding that your specific notice type is subject to them. For someone holding a document they cannot identify, at 10 PM, a directory of programs is useless without first knowing what they are looking for."*

**Statement 2:**
*"Other teams will build a chatbot that answers tenant rights questions. EvictAware builds a time-ordered action plan generator instead — because the difference between 'here is information about your rights' and 'here is what you must do in the next 24 hours, in this sequence, with this deadline displayed in a box you cannot miss' is the difference between a renter who feels informed and a renter who actually stays in their home."*

**Statement 3:**
*"Other teams will build for awareness — teaching users about tenant rights in general. EvictAware builds for the moment — designing specifically for someone under acute psychological stress at midnight, whose reading comprehension is impaired, who cannot process a paragraph of legal text, and who needs one bold statement, three action cards, and one phone number. We designed not for the average user, but for the user in the worst moment of their housing stability — because that is the exact moment when the design of information determines whether someone keeps their home."*

---

## LOCKED CONCEPT SUMMARY
### *(400 words — paste this as context into all future build prompts)*

---

**EvictAware — California Tenant Rights Navigator**
USAII Global AI Hackathon 2026 | Challenge Brief 4 | Undergraduate Track | Team Vision Forge

---

**One-Line Pitch:**
We are building an AI-powered solution that helps a California renter who just received an eviction notice and has no immediate access to legal counsel so they can identify exactly what type of notice they received, understand their legal rights in plain language, and take the right next step in the next 24 hours — without needing a lawyer, a legal dictionary, or a business-hours hotline.

**The User:**
Priya Sharma, 29, Fresno, California — part-time medical billing specialist, Uber Eats driver, single mother of a 7-year-old — found a 3-Day Notice to Pay Rent or Quit taped to her door at 9:47 PM on a Tuesday, $340 short on rent. Without EvictAware, she texts her landlord "I'll be out Friday," voluntarily vacating a home she had the legal right to keep.

**The Problem:**
California renters receiving eviction notices cannot quickly identify what type of notice they received, what rights still protect them, or what they must do in the next 24–72 hours — causing tens of thousands to self-vacate or miss legal deadlines before ever reaching a courtroom. The decision window is 24–72 hours from receipt; after that, options close permanently.

**Why AI:**
- A decision tree for California's 9+ legally distinct notice types would require 200+ branches and cannot process "I got a paper that says three days" — NLP is required
- Rules-based systems retrieve information; only contextual reasoning determines WHICH rights apply to THIS notice type in THIS location with THESE user conditions
- Information without sequence is not actionable under stress — priority generation transforms a set of rights into a time-ordered plan that tells Priya what to do first

**Three-Stage Architecture:**
Stage 1: NLP reads the user's free-text description, identifies notice type, and presents a mandatory confirmation gate before any action plan renders. Stage 2: Confirmed notice type triggers contextual legal reasoning — California Civil Code and CCP rules plus local ordinance overlays for the user's city. Stage 3: Time-ordered action plan generated in three urgency tiers with Grade 7 language, isolated deadline display, and county-specific legal aid contacts from 211.org public data.

**Three Wow Moments:**
- The Bold Statement Card: *"This notice is NOT an order to leave"* — directly neutralizes the false belief driving catastrophic wrong action
- The "What Your Landlord CANNOT Do Right Now" module: eliminates panic about immediate physical removal with specific legal authority
- The Local Legal Aid Connector: not a directory link — a specific phone number, hours, and intake link for Priya's county, populated from public data

**Four Responsible AI Elements:**
- State Scope Lock: architectural stop at entry — no California confirmation, no system access
- Confirmation Step: action plan blocked until user confirms AI's notice type classification matches their document
- Mandatory Legal Aid Acknowledgment: user must actively dismiss a limitation statement before any action plan renders
- Language Safety Validation: prohibited certainty phrases screened before output renders; all legal assessments use required uncertainty framing templates

**Impact in Numbers:**
- California processes 500,000+ unlawful detainer filings annually; 20–35% of renters self-vacate without ever reaching court
- Renters have legal representation in 3–10% of eviction proceedings; landlords in 80–90% — EvictAware narrows the information half of this gap

**Organization Inspirations:**
- **Code for America** — EvictAware's free-text single-question entry point is directly inspired by GetCalFresh's design principle: start where the user is, in their own language
- **Benefits Data Trust** — EvictAware's Local Legal Aid Connector (specific phone number, not a directory link) applies BDT's finding that a direct contact dramatically increases the rate at which people in need actually reach help

---

*Document Version: June 16, 2026 | Team Vision Forge | EvictAware*
*All sections submission-ready for Devpost, pitch video script, and demo walkthrough*
