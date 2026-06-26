# extractors/xml_extractor.py

import re
import xmltodict


def extract_xml_event(log_text, event_name):
    """
    Extrait le XML correspondant à un événement.
    """

    pattern = rf"<{event_name}>(.*?)</{event_name}>"

    match = re.search(
        pattern,
        log_text,
        re.DOTALL
    )

    if match:

        xml = f"<{event_name}>{match.group(1)}</{event_name}>"

        return xml

    return None


def xml_to_dict(xml_text):
    """
    Convertit un XML en dictionnaire Python.
    """

    if xml_text is None:
        return None

    data = xmltodict.parse(xml_text)

    return data


def extract_all_xml(log_text, events):
    """
    Extrait tous les événements XML présents.
    """

    extracted = {}

    for event in events:

        xml = extract_xml_event(log_text, event)

        if xml:

            extracted[event] = xml_to_dict(xml)[event]

    return extracted