# parsers/iso8583_parser.py

import re

from utils.constants import ISO_FIELDS
from utils.iso_utils import decode_emv


class ISO8583Parser:

    def __init__(self):

        self.fields = {}

    def parse(self, log_text):

        """
        Parse le dump ISO8583 contenu dans le log.
        """

        self.fields = {}

        for field, pattern in ISO_FIELDS.items():

            match = re.search(
                pattern,
                log_text
            )

            if match:

                self.fields[field] = match.group(1).strip()

        # Décodage du champ EMV (DE55)

        if "DE55" in self.fields:

            self.fields["EMV"] = decode_emv(
                self.fields["DE55"]
            )

        return self.fields


def parse_iso8583(log_text):

    parser = ISO8583Parser()

    return parser.parse(log_text)