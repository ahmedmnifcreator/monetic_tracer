# parsers/recording_parser.py

from utils.helpers import get_value


class RecordingParser:

    """
    Parser de :

        - RecordingRequest
        - RecordingResponse
    """

    #########################################################
    # RecordingRequest
    #########################################################

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
        # Token
        ####################################################

        token = get_value(
            data,
            ["Token"],
            {}
        )

        result["Token"] = {

            "TokenType":
                token.get("TokenType"),

            "TokenValue":
                token.get("TokenValue")

        }

        ####################################################
        # Card
        ####################################################

        card = get_value(
            data,
            ["Card"],
            {}
        )

        result["Card"] = {

            "Pan":
                card.get("Pan"),

            "IsPresent":
                card.get("IsPresent"),

            "PinControled":
                card.get("PinControled"),

            "ExpiryDate":
                card.get("ExpiryDate"),

            "LanguagePreference":
                card.get("LanguagePreference"),

            "Track2":
                card.get("Track2"),

            "P2pe": {

                "Ksn":
                    get_value(
                        card,
                        ["P2pe", "Ksn"]
                    ),

                "Bitmap":
                    get_value(
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

            "IsPresent":
                holder.get("IsPresent"),

            "VerifyMethod":
                holder.get("VerifyMethod")

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

                "Amount":
                    get_value(
                        trx,
                        ["RequestedAmount", "Amount"]
                    ),

                "Currency":
                    get_value(
                        trx,
                        ["RequestedAmount", "Currency"]
                    )

            },

            ################################################
            # ApprovedAmount
            ################################################

            "ApprovedAmount": {

                "Amount":
                    get_value(
                        trx,
                        ["ApprovedAmount", "Amount"]
                    ),

                "Currency":
                    get_value(
                        trx,
                        ["ApprovedAmount", "Currency"]
                    )

            },

            ################################################
            # FinalAmount
            ################################################

            "FinalAmount": {

                "Amount":
                    get_value(
                        trx,
                        ["FinalAmount", "Amount"]
                    ),

                "Currency":
                    get_value(
                        trx,
                        ["FinalAmount", "Currency"]
                    )

            },

            ################################################

            "PointOfServiceCondition":
                trx.get("PointOfServiceCondition"),

            "AuthorizationReason":
                trx.get("AuthorizationReason"),

            "TransactionRef":
                trx.get("TransactionRef"),

            "AuthorizationEntity":
                trx.get("AuthorizationEntity"),

            "ForcingMode":
                trx.get("ForcingMode"),

            "OriginalTransactionType":
                trx.get("OriginalTransactionType"),

            "MicroCircuitIncident":
                trx.get("MicroCircuitIncident"),

            "OfflineMode":
                trx.get("OfflineMode"),

            "FallBackIndicator":
                trx.get("FallBackIndicator"),

            "EntryMode":
                trx.get("EntryMode"),

            "PinEntryCapability":
                trx.get("PinEntryCapability"),

            "ApplicationSelection":
                trx.get("ApplicationSelection"),

            "BrandSelected":
                trx.get("BrandSelected"),

            "AcquirerId":
                trx.get("AcquirerId"),

            "ContractNumber":
                trx.get("ContractNumber"),

            "Nlsa":
                trx.get("Nlsa"),

            "MerchantUid":
                trx.get("MerchantUid"),

            "AuthorizationValue":
                trx.get("AuthorizationValue"),

            "AuthorizationResponseCode":
                trx.get("AuthorizationResponseCode"),

            "AcquirerResponseCode":
                trx.get("AcquirerResponseCode"),

            "TransactionStatus":
                trx.get("TransactionStatus"),

            "UserData":
                trx.get("UserData"),

            "RetreivalReferenceNumber":
                trx.get("RetreivalReferenceNumber"),

            "AuthorizationDateTime":
                trx.get("AuthorizationDateTime"),

            "TransactionUuid":
                trx.get("TransactionUuid"),

            "AcqTrxId":
                trx.get("AcqTrxId"),

            "PinEntered":
                trx.get("PinEntered"),

            "JcbLegacy":
                trx.get("JcbLegacy"),

            "DeferredClearing":
                trx.get("DeferredClearing"),

            "CardholderReceipt":
                trx.get("CardholderReceipt"),

            "MerchantReceipt":
                trx.get("MerchantReceipt"),

            "EmvFields":
                trx.get("EmvFields", []),

            "CbFields":
                trx.get("CbFields", [])

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

    #########################################################
    # RecordingResponse
    #########################################################

    def parse_response(self, data):

        if data is None:
            return None

        result = {

            "TransactionUuid":
                data.get("TransactionUuid"),

            "ResponseCode":
                data.get("ResponseCode"),

            "NextTransactionID":
                data.get("NextTransactionID")

        }

        return result


#########################################################
# Instance unique du parser
#########################################################

_parser = RecordingParser()


#########################################################
# Fonctions publiques
#########################################################

def parse_recording_request(data):

    """
    Parse un RecordingRequest
    """
    return _parser.parse_request(data)


def parse_recording_response(data):

    """
    Parse un RecordingResponse
    """
    return _parser.parse_response(data)