from models.transaction import Transaction

transaction = Transaction()

transaction.TransactionUuid = "364555b1-f029-40aa-83a7-b91e995ac0cc"

transaction.RiskManagementRequest = risk_request

transaction.RiskManagementResponse = risk_response

transaction.AuthorizationRequest = auth_request

transaction.AuthorizationResponse = auth_response

transaction.RecordingRequest = recording_request

transaction.RecordingResponse = recording_response

transaction.ISO8583 = iso_data

print(transaction.to_dict())