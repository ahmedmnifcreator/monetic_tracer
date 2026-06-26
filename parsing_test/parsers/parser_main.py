# parsers/parser_main.py

import json
import os

from parsers.log_reader import LogReader
from parsers.iso8583_parser import parse_iso8583

from parsers.risk_management_parser import (
    parse_risk_management_request,
    parse_risk_management_response
)

from parsers.authorization_parser import (
    parse_authorization_request,
    parse_authorization_response
)

from parsers.recording_parser import (
    parse_recording_request,
    parse_recording_response
)

from extractors.event_detector import EventDetector
from extractors.json_extractors import JsonExtractor

from models.transaction import Transaction


############################################################
# Lecture du log
############################################################

reader = LogReader("logs/log1.txt")

log = reader.read()

############################################################
# Création de la transaction
############################################################

transaction = Transaction()

############################################################
# Détection des événements
############################################################

events = EventDetector.detect_events(log)

print("Evénements détectés :")

for e in events:
    print("  -", e)

############################################################
# RiskManagementRequest
############################################################

if "RiskManagementRequest" in events:

    json_text = EventDetector.extract_json_block(
        log,
        "RiskManagementRequest"
    )

    data = JsonExtractor.parse(json_text)
    print("\n==========================")
    print(events)
    print("==========================")
    print(json_text)
    print("==========================")

    transaction.RiskManagementRequest = \
        parse_risk_management_request(data)

############################################################
# RiskManagementResponse
############################################################

if "RiskManagementResponse" in events:

    json_text = EventDetector.extract_json_block(
        log,
        "RiskManagementResponse"
    )

    data = JsonExtractor.parse(json_text)

    transaction.RiskManagementResponse = \
        parse_risk_management_response(data)

############################################################
# AuthorizationRequest
############################################################

if "AuthorizationRequest" in events:

    json_text = EventDetector.extract_json_block(
        log,
        "AuthorizationRequest"
    )

    data = JsonExtractor.parse(json_text)

    transaction.AuthorizationRequest = \
        parse_authorization_request(data)

############################################################
# AuthorizationResponse
############################################################

if "AuthorizationResponse" in events:

    json_text = EventDetector.extract_json_block(
        log,
        "AuthorizationResponse"
    )

    data = JsonExtractor.parse(json_text)

    transaction.AuthorizationResponse = \
        parse_authorization_response(data)

############################################################
# RecordingRequest
############################################################

if "RecordingRequest" in events:

    json_text = EventDetector.extract_json_block(
        log,
        "RecordingRequest"
    )

    data = JsonExtractor.parse(json_text)

    transaction.RecordingRequest = \
        parse_recording_request(data)

############################################################
# RecordingResponse
############################################################

if "RecordingResponse" in events:

    json_text = EventDetector.extract_json_block(
        log,
        "RecordingResponse"
    )

    data = JsonExtractor.parse(json_text)

    transaction.RecordingResponse = \
        parse_recording_response(data)

############################################################
# ISO8583
############################################################

transaction.ISO8583 = parse_iso8583(log)

############################################################
# Transaction UUID
############################################################

uuid = None

if transaction.RiskManagementRequest:

    uuid = transaction.RiskManagementRequest["Transaction"].get(
        "TransactionUuid"
    )

elif transaction.AuthorizationRequest:

    uuid = transaction.AuthorizationRequest["Transaction"].get(
        "TransactionUuid"
    )

elif transaction.RecordingRequest:

    uuid = transaction.RecordingRequest["Transaction"].get(
        "TransactionUuid"
    )

transaction.TransactionUuid = uuid

############################################################
# Sauvegarde JSON
############################################################

os.makedirs("output", exist_ok=True)

with open(
    "output/result.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(

        transaction.__dict__,

        f,

        indent=4,

        ensure_ascii=False

    )

############################################################

print("\nTransaction extraite avec succès.")

print("\nRésultat sauvegardé dans : output/result.json")