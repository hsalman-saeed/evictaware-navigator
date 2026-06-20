"""
Cache date updater for EvictAware.
Rewrites hard-coded dates in the demo cache so that fallback
responses always show the current date and a correct 3-day deadline.
"""
import json
import datetime


def update_cache_dates(cache_dict: dict) -> dict:
    """
    Replace all hard-coded demo dates in the cache with
    dates relative to today.

    Original cache was authored for Friday, June 19, 2026
    with a 3-day expiry of Monday, June 22, 2026.

    If today IS June 19, 2026, dates are already correct
    and we return the dict unchanged.

    Returns the updated dict. On any error, returns
    the original dict unchanged.
    """
    try:
        today = datetime.date.today()
        notice_expiry = today + datetime.timedelta(days=3)

        # If today is the original authoring date, no changes needed
        original_date = datetime.date(2026, 6, 19)
        if today == original_date:
            return cache_dict

        # Formatted strings
        today_full = today.strftime("%A, %B %d, %Y")
        today_short = today.strftime("%A, %B %d")
        today_mdy = today.strftime("%B %d, %Y")

        expiry_full = notice_expiry.strftime("%A, %B %d, %Y")
        expiry_mdy = notice_expiry.strftime("%B %d, %Y")

        # Serialize to JSON string
        json_str = json.dumps(cache_dict, ensure_ascii=False)

        # Use hex tokens that can't appear in normal text
        T1 = "\x00T1\x00"
        T2 = "\x00T2\x00"
        T3 = "\x00T3\x00"
        T4 = "\x00T4\x00"
        T5 = "\x00T5\x00"

        # Phase 1: Replace originals → tokens (longest first)
        json_str = json_str.replace("Friday, June 19, 2026", T1)
        json_str = json_str.replace("Monday, June 22, 2026", T2)
        json_str = json_str.replace("Friday, June 19", T1)
        json_str = json_str.replace("Monday, June 22", T2)
        json_str = json_str.replace("June 19, 2026", T3)
        json_str = json_str.replace("June 22, 2026", T4)
        json_str = json_str.replace("TODAY", T5)

        # Phase 2: Replace tokens → final values
        json_str = json_str.replace(T1, today_full)
        json_str = json_str.replace(T2, expiry_full)
        json_str = json_str.replace(T3, today_mdy)
        json_str = json_str.replace(T4, expiry_mdy)
        json_str = json_str.replace(T5, today_short)

        # Parse back to dict
        return json.loads(json_str)

    except Exception:
        # Never fail — return original on any error
        return cache_dict
