
import csv
from datetime import datetime

def log_result_csv(status, metrics):
    with open("reports/test_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), status, metrics.get('voltage'), metrics.get('temp')])
