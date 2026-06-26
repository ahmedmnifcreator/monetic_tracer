# utils/iso_utils.py

import re

from utils.constants import ISO_FIELDS


def parse_iso_dump(log_text):

    result = {}

    for field, pattern in ISO_FIELDS.items():

        match = re.search(
            pattern,
            log_text
        )

        if match:

            result[field] = match.group(1).strip()

    return result


def get_emv():

    return {

        "5F24": "ExpiryDate",

        "57": "Track2",

        "95": "TVR",

        "9A": "TransactionDate",

        "9C": "TransactionType",

        "9F02": "Amount",

        "9F03": "OtherAmount",

        "9F06": "AID",

        "9F10": "IssuerApplicationData",

        "9F1A": "CountryCode",

        "9F26": "ApplicationCryptogram",

        "9F27": "CryptogramInformationData",

        "9F33": "TerminalCapabilities",

        "9F34": "CVMResult",

        "9F35": "TerminalType",

        "9F36": "ATC",

        "9F37": "UnpredictableNumber"
    }


def decode_emv(hex_string):

    """
    Cette fonction sera améliorée plus tard
    pour décoder complètement le champ DE55.
    """

    return {

        "RawData": hex_string
    }