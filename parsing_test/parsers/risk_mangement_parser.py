# parsers/risk_management_parser.py

from utils.helpers import get_value


class RiskManagementParser:

    """
    Parse :

        - RiskManagementRequest
        - RiskManagementResponse

    """

    def parse_request(self, data):

        if data is None:
            return None

        result = {}

        ####################################################
        # TransactionDateTime
        ####################################################

        result["TransactionDateTime"] = data.get(
            "TransactionDateTime"
        )

        ####################################################
        # CARD
        ####################################################

        card = get_value(
            data,
            ["Card"],
            {}
        )

        result["Card"] = {

            "Pan": card.get("Pan"),

            "IsPresent": card.get("IsPresent"),

            "ExpiryDate": card.get("ExpiryDate"),

            "Track2": card.get("Track2"),

            "FallBackIndicator": card.get(
                "FallBackIndicator"
            ),

            "P2pe": {

                "Ksn": get_value(
                    card,
                    ["P2pe", "Ksn"]
                ),

                "Bitmap": get_value(
                    card,
                    ["P2pe", "Bitmap"]
                )

            }

        }

        ####################################################
        # TRANSACTION
        ####################################################

        transaction = get_value(
            data,
            ["Transaction"],
            {}
        )

        result["Transaction"] = {

            "RequestedAmount": {

                "Amount": get_value(
                    transaction,
                    [
                        "RequestedAmount",
                        "Amount"
                    ]
                ),

                "Currency": get_value(
                    transaction,
                    [
                        "RequestedAmount",
                        "Currency"
                    ]
                )

            },

            "AcquirerId":
                transaction.get("AcquirerId"),

            "ContractNumber":
                transaction.get("ContractNumber"),

            "Nlsa":
                transaction.get("Nlsa"),

            "MerchantUid":
                transaction.get("MerchantUid"),

            "AuthorizationReason":
                transaction.get(
                    "AuthorizationReason"
                ),

            "TransactionUuid":
                transaction.get(
                    "TransactionUuid"
                ),

            "EntryMode":
                transaction.get(
                    "EntryMode"
                ),

            "TransactionRef":
                transaction.get(
                    "TransactionRef"
                ),

            "BinStatus":
                transaction.get(
                    "BinStatus"
                ),

            "JcbLegacy":
                transaction.get(
                    "JcbLegacy"
                ),

            "RefundOnline":
                transaction.get(
                    "RefundOnline"
                ),

            "UserData":
                transaction.get(
                    "UserData"
                ),

            "EmvFields":
                transaction.get(
                    "EmvFields",
                    []
                ),

            "CbFields":
                transaction.get(
                    "CbFields",
                    []
                )

        }

        ####################################################
        # POI
        ####################################################

        poi = get_value(
            data,
            ["Poi"],
            {}
        )

        result["Poi"] = {

            "EcrNumber":
                poi.get("EcrNumber"),

            "PosName":
                poi.get("PosName")

        }

        return result

    ########################################################
    ########################################################

    def parse_response(self, data):

        if data is None:
            return None

        result = {}

        ####################################################
        # Transaction
        ####################################################

        trx = get_value(
            data,
            ["Transaction"],
            {}
        )

        result["Transaction"] = {

            "CumulativeAmountExcess":

                trx.get(
                    "CumulativeAmountExcess"
                ),

            "TransactionUuid":

                trx.get(
                    "TransactionUuid"
                ),

            "DenyListLevel":

                trx.get(
                    "DenyListLevel"
                ),

            "TransactionRef":

                trx.get(
                    "TransactionRef"
                )

        }

        ####################################################
        # TOKEN
        ####################################################

        token = get_value(
            data,
            ["Token"],
            {}
        )

        result["Token"] = {

            "TokenType":
                token.get(
                    "TokenType"
                ),

            "TokenValue":
                token.get(
                    "TokenValue"
                )

        }

        ####################################################
        # ORIGINAL TRANSACTION
        ####################################################

        original = get_value(
            data,
            ["OriginalTransaction"],
            {}
        )

        result["OriginalTransaction"] = {

            "ApprovalStatus":

                original.get(
                    "ApprovalStatus"
                ),

            "AcqTrxId":

                original.get(
                    "AcqTrxId"
                ),

            "AuthorizationValue":

                original.get(
                    "AuthorizationValue"
                ),

            "ForcingMode":

                original.get(
                    "ForcingMode"
                ),

            "AppliCryptogram":

                original.get(
                    "AppliCryptogram"
                )

        }

        result["ReferenceData"] = data.get(
            "ReferenceData"
        )

        return result


##########################################################
# Fonctions publiques
##########################################################

_parser = RiskManagementParser()


def parse_risk_management_request(data):

    return _parser.parse_request(data)


def parse_risk_management_response(data):

    return _parser.parse_response(data)