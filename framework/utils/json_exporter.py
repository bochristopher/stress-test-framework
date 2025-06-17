
import json

def export_metrics(metrics, filename="reports/results.json"):
    with open(filename, "w") as f:
        json.dump(metrics, f, indent=2)
