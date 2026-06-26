# extractors/event_detector.py

import re


class EventDetector:
    """
    Détecte les différents événements présents dans le log.
    """

    EVENTS = [
        "RiskManagementRequest",
        "RiskManagementResponse",
        "AuthorizationRequest",
        "AuthorizationResponse",
        "RecordingRequest",
        "RecordingResponse"
    ]

    ############################################################

    @staticmethod
    def has_event(log, event):
        """
        Vérifie si un événement existe dans le log.
        """
        return event in log

    ############################################################

    @staticmethod
    def detect_events(log):
        """
        Retourne la liste des événements trouvés.
        """
        found = []

        for event in EventDetector.EVENTS:
            if EventDetector.has_event(log, event):
                found.append(event)

        return found

    ############################################################

    @staticmethod
    def extract_json_block(log, event):
        """
        Extrait le JSON correspondant à un événement.

        Exemple :

        RiskManagementRequest : {...}

        AuthorizationRequest : {...}
        """

        start = log.find(event)

        if start == -1:
            return None

        # Chercher la première accolade {
        start = log.find("{", start)

        if start == -1:
            return None

        count = 0
        end = start

        while end < len(log):

            if log[end] == "{":
                count += 1

            elif log[end] == "}":
                count -= 1

                if count == 0:
                    return log[start:end + 1]

            end += 1

        return None

    ############################################################

    @staticmethod
    def extract_xml_block(log, event):
        """
        Extrait un bloc XML.

        <RiskManagementRequest>
        ...
        </RiskManagementRequest>
        """

        pattern = (
            rf"<{event}>"
            r".*?"
            rf"</{event}>"
        )

        match = re.search(
            pattern,
            log,
            re.DOTALL
        )

        if match:
            return match.group()

        return None