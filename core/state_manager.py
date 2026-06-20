"""
EvictAwareStateManager — controls all conversation flow.
Implements Component 4 from EvictAware_Core_AI_Prompt_System.md.
This class owns stage transitions, emergency detection,
notice classification, and API payload assembly.
"""
import re
from datetime import date
from typing import Optional, Tuple


class EvictAwareStateManager:
    """
    Manages all conversation state for EvictAware.
    Stored in st.session_state["state_manager"].
    """

    # Stage constants
    STAGE_1_IDENTIFY = "STAGE_1_IDENTIFY"
    STAGE_2_CONFIRM = "STAGE_2_CONFIRM"
    STAGE_3_ACTION_PLAN = "STAGE_3_ACTION_PLAN"
    EMERGENCY_LOCKOUT = "EMERGENCY_LOCKOUT"
    EMERGENCY_DV = "EMERGENCY_DV"
    EMERGENCY_SHELTER = "EMERGENCY_SHELTER"
    HARD_STOP_STATE = "HARD_STOP_STATE"

    # Emergency trigger word lists — loaded here, not hardcoded in UI
    LOCKOUT_TRIGGERS = [
        "changed my locks",
        "changed the locks",
        "locked out",
        "can't get in",
        "cannot get in",
        "locked me out",
        "already removed my things",
        "removed my belongings",
        "locked me out of",
        "changed locks",
        "blocked access",
        "locks were changed",
    ]
    DV_TRIGGERS = [
        "domestic violence",
        "abuse",
        "abusive",
        "unsafe at home",
        "scared of him",
        "scared of her",
        "scared of my partner",
        "partner hurts",
        "boyfriend hurts",
        "husband hurts",
        "wife hurts",
        "controlling partner",
    ]
    SHELTER_TRIGGERS = [
        "nowhere to go",
        "kids have nowhere",
        "children will be homeless",
        "sleeping in my car",
        "no place to go",
        "my kids have no place",
        "daughter has nowhere",
        "son has nowhere",
        "children with nowhere to go",
        "homeless tonight",
        "no place to stay",
    ]

    # Non-California detection
    NON_CA_STATES = [
        "texas", "florida", "new york", "illinois", "ohio", "georgia",
        "north carolina", "michigan", "pennsylvania", "arizona", "nevada",
        "washington state", "colorado", "virginia", "massachusetts",
        "indiana", "tennessee", "missouri", "maryland", "wisconsin",
        "minnesota", "south carolina", "alabama", "louisiana", "kentucky",
        "oregon", "oklahoma", "connecticut", "utah", "iowa", "mississippi",
        "arkansas", "kansas", "new mexico", "nebraska", "idaho",
        "west virginia", "hawaii", "new hampshire", "maine",
        "rhode island", "montana", "delaware", "south dakota",
        "north dakota", "alaska", "vermont", "wyoming",
        "dallas", "houston", "chicago", "miami", "phoenix", "denver",
        "seattle", "atlanta", "boston", "detroit", "minneapolis",
        "portland", "nashville", "las vegas", "austin", "new orleans",
        "philadelphia", "charlotte", "jacksonville",
    ]

    CA_SIGNALS = [
        "california", "fresno", "los angeles", "san francisco",
        "san diego", "sacramento", "oakland", "san jose", "riverside",
        "bakersfield", "anaheim", "stockton", "modesto", "fontana",
        "fremont", "irvine", "glendale", "huntington beach", "long beach",
        "chula vista", "santa ana", "san bernardino", "redding",
        "santa barbara", "santa cruz", "ventura", "pasadena", "torrance",
        "hayward", "escondido", "sunnyvale", "pomona", "roseville",
    ]

    def __init__(self):
        self.current_stage = self.STAGE_1_IDENTIFY
        self.identified_notice_type = None
        self.confirmed_notice_type = None
        self.user_county = None
        self.reclassification_attempts = 0
        self.conversation_history = []
        self.confirmation_gate_completed = False
        self.acknowledgment_completed = False
        self.california_confirmed = False
        self.emergency_type = None
        self.ai_response_source = None
        self.user_input_text = ""
        self._stage_log = []

    def detect_emergency_overrides(self, user_input: str) -> Optional[str]:
        """
        Scan user input for emergency trigger phrases.
        Returns emergency type string or None.
        Trigger lists are defined as class constants, not hardcoded inline.
        """
        text = user_input.lower()
        for phrase in self.LOCKOUT_TRIGGERS:
            if phrase in text:
                return self.EMERGENCY_LOCKOUT
        for phrase in self.DV_TRIGGERS:
            if phrase in text:
                return self.EMERGENCY_DV
        for phrase in self.SHELTER_TRIGGERS:
            if phrase in text:
                return self.EMERGENCY_SHELTER
        return None

    def detect_california_state(self, user_input: str) -> Optional[bool]:
        """
        Returns True if California confirmed, False if another state
        detected, None if unknown.
        """
        text = user_input.lower()
        for state in self.NON_CA_STATES:
            if re.search(r"\b" + re.escape(state) + r"\b", text):
                return False
        for signal in self.CA_SIGNALS:
            if re.search(r"\b" + re.escape(signal) + r"\b", text):
                return True
        return None

    def identify_notice_type(
        self, user_input: str, notice_data: list
    ) -> Tuple[Optional[str], float, list]:
        """
        Match user input against trigger phrases and identification
        signals from california_eviction_data.json.
        Returns (notice_type_id, confidence_score, matched_signals).
        No hardcoded notice type logic — reads entirely from JSON.
        """
        text = user_input.lower()
        scores = {}
        matched = {}

        for notice in notice_data:
            notice_id = notice.get("id")
            if not notice_id:
                continue

            score = 0.0
            matches = []

            # Check trigger phrases (weight: 0.15 each)
            for phrase in notice.get("common_trigger_phrases", []):
                if phrase.lower() in text:
                    score += 0.15
                    matches.append(phrase)

            # Check AI identification signals (weight: 0.25 each)
            for signal in notice.get("ai_identification_signals", []):
                if signal.lower() in text:
                    score += 0.25
                    matches.append(signal)

            if score > 0:
                scores[notice_id] = min(score, 1.0)
                matched[notice_id] = matches

        if not scores:
            return None, 0.0, []

        best_id = max(scores, key=scores.get)
        return best_id, scores[best_id], matched.get(best_id, [])

    def advance_stage(
        self, new_stage: str, confirmed_type: str = None
    ) -> None:
        """Update stage and log the transition."""
        self._stage_log.append(
            f"{self.current_stage} -> {new_stage} "
            f"| notice: {confirmed_type or self.identified_notice_type}"
        )
        self.current_stage = new_stage
        if confirmed_type:
            self.confirmed_notice_type = confirmed_type

    def get_current_prompt_modifier(self) -> str:
        """
        Return the stage-specific instruction block added to the
        system prompt.
        """
        stage_instructions = {
            self.STAGE_1_IDENTIFY: (
                "CURRENT STAGE: STAGE 1 — IDENTIFY\n"
                "Your task: Read the user's description. "
                "If you can identify the notice type, present the "
                "Confirmation Gate. If not, ask exactly ONE clarifying "
                "question from the approved list. Do NOT generate an "
                "action plan yet."
            ),
            self.STAGE_2_CONFIRM: (
                "CURRENT STAGE: STAGE 2 — CONFIRM\n"
                f"Identified notice type: {self.identified_notice_type}\n"
                "Your task: Present the confirmation gate exactly as "
                "specified. Ask the user to confirm the notice type "
                "matches their document. Do NOT generate an action plan yet."
            ),
            self.STAGE_3_ACTION_PLAN: (
                "CURRENT STAGE: STAGE 3 — ACTION PLAN\n"
                f"Confirmed notice type: {self.confirmed_notice_type}\n"
                f"Today's date for deadline calculation: "
                f"{date.today().strftime('%A, %B %d, %Y')}\n"
                "Your task: Generate the complete action plan JSON. "
                "Follow the output schema exactly. "
                "Do NOT include markdown code fences. "
                "Output ONLY valid JSON, nothing else.\n\n"
                "REQUIRED JSON SCHEMA:\n"
                "{\n"
                '  "bold_statement_card": {"text": "...", "legal_basis": "..."},\n'
                '  "notice_summary": {"notice_type": "...", "what_it_means": "...", '
                '"does_tenant_have_to_leave_now": false, '
                '"critical_deadline": {"label": "...", "date": "...", "days_remaining": N}},\n'
                '  "action_tiers": {\n'
                '    "tier_1": {"label": "NEXT 24 HOURS", "color": "red", '
                '"urgency_reason": "...", "actions": [{"deadline": "...", '
                '"action": "...", "why_it_matters": "...", "how_to_do_it": "..."}]},\n'
                '    "tier_2": {"label": "BEFORE YOUR NOTICE EXPIRES", "color": "orange", ...},\n'
                '    "tier_3": {"label": "IF COURT PAPERS ARE FILED", "color": "yellow", ...}\n'
                "  },\n"
                '  "landlord_cannot_do": {"module_title": "...", "items": [...], '
                '"most_relevant_to_user_situation": "..."},\n'
                '  "legal_aid_connector": {"intro_text": "...", "organization_name": "...", '
                '"phone_number": "...", "hours": "...", "intake_link": "...", '
                '"languages": [...], "what_to_say_when_you_call": "..."},\n'
                '  "rental_assistance": {"applicable": true/false, "resources": [...], '
                '"important_note": "..."},\n'
                '  "disclaimer": "...",\n'
                '  "stage": "action_plan",\n'
                '  "notice_type_id": "..."\n'
                "}"
            ),
        }
        return stage_instructions.get(self.current_stage, "")

    def build_full_api_payload(
        self,
        user_message: str,
        system_prompt: str,
        context_injection: str,
    ) -> dict:
        """
        Assemble the complete API call payload.
        Returns a dict with system_instruction, contents, generation_config.
        """
        stage = self.current_stage
        full_system = (
            f"{system_prompt}\n\n"
            f"{context_injection}\n\n"
            f"{self.get_current_prompt_modifier()}"
        )

        generation_config = {
            "temperature": 0.2,
            "max_output_tokens": (
                2048 if stage == self.STAGE_3_ACTION_PLAN else 1024
            ),
        }

        return {
            "system_instruction": full_system,
            "contents": self.conversation_history
            + [{"role": "user", "parts": [{"text": user_message}]}],
            "generation_config": generation_config,
        }

    def add_to_history(self, role: str, text: str) -> None:
        """Add a message to conversation history."""
        self.conversation_history.append(
            {"role": role, "parts": [{"text": text}]}
        )

    def reset(self) -> None:
        """Reset all state to initial values."""
        self.__init__()
