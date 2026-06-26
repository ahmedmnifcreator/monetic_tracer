# extractors/json_extractor.py

import json
import re


def extract_json_event(log_text, event_name):
    """
    Extrait un objet JSON associé à un événement.
    """

    pattern = rf"{event_name}\s*:\s*(\{{.*?\}})"

    match = re.search(
        pattern,
        log_text,
        re.DOTALL
    )

    if not match:
        return None

    try:

        return json.loads(match.group(1))

    except Exception:

        return None


def extract_all_json(log_text, events):
    """
    Extrait tous les événements JSON.
    """

    extracted = {}

    for event in events:

        data = extract_json_event(
            log_text,
            event
        )

        if data:

            extracted[event] = data

    return extracted