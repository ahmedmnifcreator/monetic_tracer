import json

def extract_risk_management_requests(log_file):

    risk_requests = []

    with open(log_file, "r", encoding="utf-8") as f:

        for line in f:

            if "RiskManagementRequest:" in line:

                try:
                    json_str = line.split("RiskManagementRequest:", 1)[1].strip()

                    request = json.loads(json_str)

                    risk_requests.append(request)

                except json.JSONDecodeError:
                    print("Erreur JSON")

    return risk_requests


# Utilisation
requests = extract_risk_management_requests("solution_simple/log2.txt")

print(f"{len(requests)} transactions trouvées")

for i, req in enumerate(requests, start=1):
    print(f"\n===== RiskManagementRequest {i} =====")
    print(json.dumps(req, indent=4))