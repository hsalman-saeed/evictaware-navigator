"""
Prompt template library for EvictAware.
Implements Component 6 from EvictAware_Core_AI_Prompt_System.md.
All templates read from this library — never written inline in app logic.
"""


PROMPTS = {
    "P1-A": (
        "Welcome to EvictAware. I'll help you understand the notice "
        "you received and what to do next. Please describe the notice "
        "in your own words — what does it say? It's okay if you don't "
        "know the legal terms."
    ),
    "P1-B": (
        "I want to make sure I understand your notice correctly. "
        "Does your notice mention a specific number of days — "
        "like 3 days, 30 days, or 60 days?"
    ),
    "P1-C": (
        "I want to be accurate for you. Does your notice give you "
        "the option to pay money to stay — or does it say you must "
        "leave regardless of payment?"
    ),
    "P1-D": (
        "Has your landlord already filed paperwork at the courthouse, "
        "or did you receive a paper taped to your door or handed to you?"
    ),
    "P1-E": (
        "It sounds like you may have received more than one notice. "
        "Can you describe the most recent one — the one you received last?"
    ),
    "PE-A": (
        "IMPORTANT: What you are describing — a landlord changing your "
        "locks or removing your belongings — is illegal in California, "
        "even if you owe rent. This is called an illegal lockout.\n\n"
        "Do these things RIGHT NOW:\n"
        "1. Call the police non-emergency line and report an illegal "
        "lockout. Ask them to document it.\n"
        "2. Take photos or screenshots of any messages from your landlord.\n"
        "3. Call 211 and ask for tenant rights emergency assistance.\n"
        "4. Tomorrow morning, call your county legal aid office.\n\n"
        "You MAY be entitled to damages under California Civil Code "
        "Section 789.3. Do not leave your home voluntarily."
    ),
    "PE-B": (
        "Your safety is the first priority. "
        "If you are in immediate danger, call 911.\n\n"
        "For domestic violence housing help, contact:\n"
        "National DV Hotline: 1-800-799-7233 (available 24/7)\n"
        "Text START to 88788\n\n"
        "They can help with safe housing options regardless of your "
        "eviction situation. Once you are safe, I can help you "
        "understand your housing rights."
    ),
    "PE-C": (
        "I hear you — you and your children need a safe place to stay. "
        "Call 211 right now from any phone, at no cost, 24 hours a day. "
        "Ask for emergency shelter. They can help you tonight.\n\n"
        "Once shelter is arranged, I can help you understand your "
        "rights regarding the eviction notice."
    ),
    "PH-A": (
        "EvictAware covers California tenant rights only. "
        "It looks like you may be in a different state.\n\n"
        "For tenant rights help in your state:\n"
        "- Call 211 from any phone — free, available in all 50 states\n"
        "- Visit lawhelp.org to find free legal aid in your state\n"
        "- Contact your state's housing authority\n\n"
        "Each state has different eviction laws and timelines. "
        "Using California information for another state could give "
        "you the wrong guidance."
    ),
    "PH-B": (
        "I want to give you accurate guidance, and I need a bit more "
        "information to identify your notice type correctly.\n\n"
        "Here are the notice types EvictAware can help with. "
        "Which one best describes what your notice says?"
    ),
    "PH-C": (
        "EvictAware is experiencing a technical issue right now. "
        "I'm not able to process your request at this moment.\n\n"
        "For immediate help with your eviction notice:\n"
        "- Call 211 — free, available 24/7\n"
        "- Visit courts.ca.gov/selfhelp for California eviction "
        "information\n"
        "- Call your county legal aid office in the morning\n\n"
        "Please try EvictAware again in a few minutes."
    ),
}


def get_prompt(prompt_id: str, **kwargs) -> str:
    """
    Return a prompt template by ID, substituting any keyword arguments.
    Raises KeyError if prompt_id not found.
    """
    template = PROMPTS.get(prompt_id)
    if template is None:
        raise KeyError(f"Prompt ID '{prompt_id}' not found in library.")

    for key, value in kwargs.items():
        template = template.replace(f"[{key.upper()}]", str(value))

    return template
