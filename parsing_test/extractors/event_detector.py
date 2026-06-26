# extractors/event_detector.py

from utils.constants import EVENTS


def detect_events(log_text):
    """
    Retourne la liste des événements présents dans le log.
    """

    detected_events = []

    for event in EVENTS:

        if event in log_text:
            detected_events.append(event)

    return detected_events