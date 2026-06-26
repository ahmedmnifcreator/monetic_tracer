# utils/constants.py

EVENTS = [

    "RiskManagementRequest",
    "RiskManagementResponse",

    "AuthorizationRequest",
    "AuthorizationResponse",

    "RecordingRequest",
    "RecordingResponse"
]


ISO_FIELDS = {

    "MTI": r"\[000\]\s+(\S+)",

    "DE2": r"\[002\]\s+(.+)",

    "DE3": r"\[003\]\s+(.+)",

    "DE4": r"\[004\]\s+(.+)",

    "DE7": r"\[007\]\s+(.+)",

    "DE11": r"\[011\]\s+(.+)",

    "DE12": r"\[012\]\s+(.+)",

    "DE13": r"\[013\]\s+(.+)",

    "DE18": r"\[018\]\s+(.+)",

    "DE22": r"\[022\]\s+(.+)",

    "DE23": r"\[023\]\s+(.+)",

    "DE25": r"\[025\]\s+(.+)",

    "DE32": r"\[032\]\s+(.+)",

    "DE35": r"\[035\]\s+(.+)",

    "DE37": r"\[037\]\s+(.+)",

    "DE38": r"\[038\]\s+(.+)",

    "DE39": r"\[039\]\s+(.+)",

    "DE41": r"\[041\]\s+(.+)",

    "DE42": r"\[042\]\s+(.+)",

    "DE47": r"\[047\]\s+(.+)",

    "DE49": r"\[049\]\s+(.+)",

    "DE53": r"\[053\]\s+(.+)",

    "DE54": r"\[054\]\s+(.+)",

    "DE55": r"\[055\]\s+(.+)",

    "DE59": r"\[059\]\s+(.+)"
}