# parsers/authorization_parser.py

from utils.helpers import get_value


class AuthorizationParser:

    """
    Parser des événements :

        - AuthorizationRequest
        - AuthorizationResponse
    """

    ####################################################
    # AuthorizationRequest
    ####################################################

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
        # Card
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

            "PinControled": card.get("PinControled"),

            "LanguagePreference": card.get(
                "LanguagePreference"
            ),

            "Track2": card.get("Track2"),

            "PinData": {

                "EncryptedPinData": get_value(
                    card,
                    ["PinData", "EncryptedPinData"]
                ),

                "PinFormat": get_value(
                    card,
                    ["PinData", "PinFormat"]
                ),

                "EncryptedPinKsn": get_value(
                    card,
                    ["PinData", "EncryptedPinKsn"]
                )

            },

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
        # CardHolder
        ####################################################

        holder = get_value(
            data,
            ["CardHolder"],
            {}
        )

        result["CardHolder"] = {

            "IsPresent": holder.get(
                "IsPresent"
            ),

            "VerifyMethod": holder.get(
                "VerifyMethod"
            )

        }

        ####################################################
        # Transaction
        ####################################################

        trx = get_value(
            data,
            ["Transaction"],
            {}
        )

        result["Transaction"] = {

            ################################################
            # RequestedAmount
            ################################################

            "RequestedAmount": {

                "Amount": get_value(
                    trx,
                    [
                        "RequestedAmount",
                        "Amount"
                    ]
                ),

                "Currency": get_value(
                    trx,
                    [
                        "RequestedAmount",
                        "Currency"
                    ]
                )

            },

            ################################################

            "PointOfServiceCondition":
                trx.get(
                    "PointOfServiceCondition"
                ),

            "AuthorizationReason":
                trx.get(
                    "AuthorizationReason"
                ),

            "FallBackIndicator":
                trx.get(
                    "FallBackIndicator"
                ),

            "ForcingMode":
                trx.get(
                    "ForcingMode"
                ),

            "MicroCircuitIncident":
                trx.get(
                    "MicroCircuitIncident"
                ),

            "EntryMode":
                trx.get(
                    "EntryMode"
                ),

            "PinEntryCapability":
                trx.get(
                    "PinEntryCapability"
                ),

            "ApplicationSelection":
                trx.get(
                    "ApplicationSelection"
                ),

            "BrandSelected":
                trx.get(
                    "BrandSelected"
                ),

            "AcquirerId":
                trx.get(
                    "AcquirerId"
                ),

            "ContractNumber":
                trx.get(
                    "ContractNumber"
                ),

            "Nlsa":
                trx.get(
                    "Nlsa"
                ),

            "MerchantUid":
                trx.get(
                    "MerchantUid"
                ),

            "UserData":
                trx.get(
                    "UserData"
                ),

            "RetreivalReferenceNumber":
                trx.get(
                    "RetreivalReferenceNumber"
                ),

            "TransactionUuid":
                trx.get(
                    "TransactionUuid"
                ),

            "TransactionRef":
                trx.get(
                    "TransactionRef"
                ),

            "SingleTap":
                trx.get(
                    "SingleTap"
                ),

            "AcqTrxId":
                trx.get(
                    "AcqTrxId"
                ),

            "PinEntered":
                trx.get(
                    "PinEntered"
                ),

            "JcbLegacy":
                trx.get(
                    "JcbLegacy"
                ),

            "DeferredClearing":
                trx.get(
                    "DeferredClearing"
                ),

            "EmvFields":
                trx.get(
                    "EmvFields",
                    []
                ),

            "CbFields":
                trx.get(
                    "CbFields",
                    []
                )

        }
            ####################################################
        # Order
        ####################################################

        order = get_value(
            data,
            ["Order"],
            {}
        )

        result["Order"] = {

            "Origin": order.get(
                "Origin"
            )

        }

        ####################################################
        # Poi
        ####################################################

        poi = get_value(
            data,
            ["Poi"],
            {}
        )

        result["Poi"] = {

            "PosName":
                poi.get("PosName"),

            "EcrNumber":
                poi.get("EcrNumber"),

            "AdditionalCardReadingCapability":
                poi.get(
                    "AdditionalCardReadingCapability"
                ),

            "PointOfInteractionInformation":
                poi.get(
                    "PointOfInteractionInformation"
                )

        }

        ####################################################
        # ReferenceData
        ####################################################

        result["ReferenceData"] = data.get(
            "ReferenceData"
        )

        return result

    ####################################################
    # AuthorizationResponse
    ####################################################

    def parse_response(self, data):

        if data is None:
            return None

        result = {}

        trx = get_value(
            data,
            ["Transaction"],
            {}
        )

        result["Transaction"] = {

            "TransactionRef":
                trx.get(
                    "TransactionRef"
                ),

            "AuthorizationValue":
                trx.get(
                    "AuthorizationValue"
                ),

            "AuthorizationResponseCode":
                trx.get(
                    "AuthorizationResponseCode"
                ),

            "AcquirerResponseCode":
                trx.get(
                    "AcquirerResponseCode"
                ),

            "TransactionStatus":
                trx.get(
                    "TransactionStatus"
                ),

            "ApprovedAmount": {

                "Amount": get_value(
                    trx,
                    [
                        "ApprovedAmount",
                        "Amount"
                    ]
                ),

                "Currency": get_value(
                    trx,
                    [
                        "ApprovedAmount",
                        "Currency"
                    ]
                )

            },

            "AccptPointMsg": {

                "Destination": get_value(
                    trx,
                    [
                        "AccptPointMsg",
                        "Destination"
                    ]
                ),

                "Message": get_value(
                    trx,
                    [
                        "AccptPointMsg",
                        "Message"
                    ]
                )

            },

            "EmvFields":
                trx.get(
                    "EmvFields",
                    []
                ),

            "TransactionUuid":
                trx.get(
                    "TransactionUuid"
                ),

            "RetreivalReferenceNumber":
                trx.get(
                    "RetreivalReferenceNumber"
                ),

            "PhoneNumber":
                trx.get(
                    "PhoneNumber"
                ),

            "AuthorizationDateTime":
                trx.get(
                    "AuthorizationDateTime"
                ),

            "AcqTrxId":
                trx.get(
                    "AcqTrxId"
                )

        }

        result["ReferenceData"] = data.get(
            "ReferenceData"
        )

        return result


#############################################################
# Instance unique du parser
#############################################################

_parser = AuthorizationParser()


#############################################################
# Fonctions publiques
#############################################################

def parse_authorization_request(data):

    return _parser.parse_request(data)


def parse_authorization_response(data):

    return _parser.parse_response(data)