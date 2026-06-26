# models/transaction.py

class Transaction:

    def __init__(self):

        self.TransactionUuid = None

        self.RiskManagementRequest = None
        self.RiskManagementResponse = None

        self.AuthorizationRequest = None
        self.AuthorizationResponse = None

        self.RecordingRequest = None
        self.RecordingResponse = None

        self.ISO8583 = None

    def to_dict(self):

        return {

            "TransactionUuid": self.TransactionUuid,

            "RiskManagementRequest": self.RiskManagementRequest,

            "RiskManagementResponse": self.RiskManagementResponse,

            "AuthorizationRequest": self.AuthorizationRequest,

            "AuthorizationResponse": self.AuthorizationResponse,

            "RecordingRequest": self.RecordingRequest,

            "RecordingResponse": self.RecordingResponse,

            "ISO8583": self.ISO8583
        }