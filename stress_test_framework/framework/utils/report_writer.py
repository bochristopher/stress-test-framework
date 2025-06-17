
def write_html_report(status, metrics, attempts, error=None):
    html = f"""<html><head><title>Test Report</title></head><body>
    <h1>Stress Rack Test Report</h1>
    <p><strong>Status:</strong> {status}</p>
    <p><strong>Attempts:</strong> {attempts}</p>
    <p><strong>Voltage:</strong> {metrics['voltage']} V</p>
    <p><strong>Temperature:</strong> {metrics['temp']} °C</p>"""

    if error:
        html += f"<p><strong>Error:</strong> {error}</p>"

    html += "</body></html>"

    with open("reports/test_report.html", "w") as f:
        f.write(html)
