"""
EvictAwareOutputValidator — validates every AI response before display.
Implements Component 5 from EvictAware_Core_AI_Prompt_System.md.
Prohibited phrases are loaded from ai_config.json — not hardcoded here.
"""
import json
import re
from typing import Optional


class EvictAwareOutputValidator:
    """
    Validates AI outputs before they reach the user.
    Loads all rules from ai_config.json.
    """

    def __init__(self, config_data: dict):
        self.config = config_data
        self.prohibited_phrases = self._load_prohibited_phrases(config_data)
        self.mandatory_disclaimer = config_data.get(
            "mandatory_disclaimer_text", ""
        )
        self.max_actions_per_tier = 3
        self.validation_log = []

    def _load_prohibited_phrases(self, config_data: dict) -> list:
        """
        Load prohibited phrases from ai_config.json.
        Returns flat list of {prohibited, allowed} dicts.
        """
        all_phrases = []
        phrase_config = config_data.get("prohibited_output_phrases", {})

        if isinstance(phrase_config, dict):
            for category, phrases in phrase_config.items():
                if isinstance(phrases, list):
                    for item in phrases:
                        if isinstance(item, dict) and "prohibited" in item:
                            all_phrases.append(item)

        return all_phrases

    def validate_json_structure(self, response_text: str) -> tuple:
        """
        Attempt to parse response as JSON and check required fields.
        Returns (is_valid, parsed_dict_or_None, error_message_or_None).
        """
        clean = response_text.strip()
        # Strip markdown code fences if AI included them
        clean = re.sub(r"^```(?:json)?\s*", "", clean)
        clean = re.sub(r"\s*```$", "", clean)
        clean = clean.strip()

        try:
            parsed = json.loads(clean)
        except json.JSONDecodeError as e:
            return False, None, f"Invalid JSON: {e}"

        required_fields = [
            "bold_statement_card",
            "action_tiers",
            "landlord_cannot_do",
            "legal_aid_connector",
            "disclaimer",
        ]
        missing = [f for f in required_fields if f not in parsed]
        if missing:
            return False, None, f"Missing required fields: {missing}"

        return True, parsed, None

    def check_prohibited_phrases(self, response_text: str) -> list:
        """
        Scan response for all prohibited phrases.
        Returns list of found prohibited phrase strings.
        """
        text_lower = response_text.lower()
        found = []
        for item in self.prohibited_phrases:
            prohibited = item.get("prohibited", "")
            if prohibited and prohibited.lower() in text_lower:
                found.append(prohibited)
        return found

    def check_action_count(self, action_plan_json: dict) -> bool:
        """
        Verify no tier has more than 3 action items.
        Returns True if valid.
        """
        tiers = action_plan_json.get("action_tiers", {})
        for tier_key, tier_data in tiers.items():
            if isinstance(tier_data, dict):
                actions = tier_data.get("actions", [])
                if len(actions) > self.max_actions_per_tier:
                    return False
        return True

    def check_disclaimer_present(self, response_text: str) -> bool:
        """Check if mandatory disclaimer text is present."""
        if not self.mandatory_disclaimer:
            return True
        # Check for the first 10 words of the disclaimer
        first_words = " ".join(self.mandatory_disclaimer.split()[:10]).lower()
        return first_words in response_text.lower()

    def check_legal_aid_present(self, action_plan_json: dict) -> bool:
        """Verify legal_aid_connector section is populated."""
        connector = action_plan_json.get("legal_aid_connector", {})
        if not connector:
            return False
        has_info = bool(
            connector.get("phone_number")
            or connector.get("organization_name")
        )
        return has_info

    def check_no_outcome_predictions(self, response_text: str) -> list:
        """Scan for phrases that predict court outcomes."""
        prediction_patterns = [
            r"\byou will win\b",
            r"\byou'll win\b",
            r"\bguaranteed\b",
            r"\bwill definitely\b",
            r"\bjudge will rule in your favor\b",
            r"\byou cannot be evicted\b",
        ]
        found = []
        text_lower = response_text.lower()
        for pattern in prediction_patterns:
            if re.search(pattern, text_lower):
                found.append(pattern)
        return found

    def build_reprompt_instruction(self, failures: list) -> str:
        """
        Generate a specific re-prompt instruction for the AI.
        Tells the AI exactly what to fix.
        """
        instructions = [
            "Your previous response had the following problems. "
            "Please rewrite your response fixing ALL of these issues:"
        ]
        for failure in failures:
            instructions.append(f"- {failure}")
        instructions.append(
            "Remember: Output ONLY valid JSON. "
            "No markdown fences. No prohibited phrases. "
            "Include the mandatory disclaimer in the 'disclaimer' field."
        )
        return "\n".join(instructions)

    def run_full_validation(
        self, response_text: str, expected_stage: str
    ) -> dict:
        """
        Run all validation checks.
        Returns validation result dict with action recommendation.
        """
        result = {
            "is_valid": True,
            "json_parsed": None,
            "failures": [],
            "action": "display",
            "re_prompt_instruction": None,
        }

        # For Stage 3: validate JSON structure
        if expected_stage == "STAGE_3_ACTION_PLAN":
            is_valid_json, parsed, error = self.validate_json_structure(
                response_text
            )
            if not is_valid_json:
                result["failures"].append(f"JSON structure error: {error}")
                result["is_valid"] = False
            else:
                result["json_parsed"] = parsed

                # Check action count
                if not self.check_action_count(parsed):
                    result["failures"].append(
                        "One or more tiers exceed 3 action items. "
                        "Reduce to maximum 3 actions per tier."
                    )
                    result["is_valid"] = False

                # Check legal aid present
                if not self.check_legal_aid_present(parsed):
                    result["failures"].append(
                        "legal_aid_connector section is missing or empty. "
                        "Include the county legal aid contact information."
                    )
                    result["is_valid"] = False

        # Check prohibited phrases (all stages)
        prohibited_found = self.check_prohibited_phrases(response_text)
        if prohibited_found:
            result["failures"].append(
                f"Prohibited certainty phrases found: {prohibited_found}. "
                f"Replace all certainty language with 'MAY' framing."
            )
            result["is_valid"] = False

        # Check outcome predictions (all stages)
        predictions = self.check_no_outcome_predictions(response_text)
        if predictions:
            result["failures"].append(
                f"Outcome predictions detected: {predictions}. "
                f"Remove all outcome predictions."
            )
            result["is_valid"] = False

        # Determine action
        if not result["is_valid"]:
            result["action"] = "re_prompt"
            result["re_prompt_instruction"] = (
                self.build_reprompt_instruction(result["failures"])
            )

        self.validation_log.append(result)
        return result
