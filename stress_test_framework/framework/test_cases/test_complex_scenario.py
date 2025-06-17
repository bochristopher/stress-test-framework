
from framework.automation.stress_rack_controller import StressRackController
from framework.test_cases.mock_system_check import check_system_alive
from framework.utils.logger import log
from framework.utils.data_collector import collect_metrics
from framework.utils.report_writer import write_html_report
from framework.utils.csv_logger import log_result_csv
from framework.utils.json_exporter import export_metrics
from framework.hardware.mock_hal import MockHAL
from framework.utils.timer import Timer

def complex_stress_test():
    racks = ["Rack-1", "Rack-2", "Rack-3"]
    hal = MockHAL()

    for rack_id in racks:
        log(f"🚦 Starting test for {rack_id}")
        rack = StressRackController(rack_id)
        hal.power_off()
        hal.power_on()

        for temp in range(40, 70, 10):  # Stepwise thermal test
            log(f"🌡️ Setting temperature to {temp}C")
            rack.set_temperature(temp)

        with Timer() as t:
            metrics = collect_metrics()
            recovered = check_system_alive()

        status = "PASS" if recovered else "FAIL"
        log(f"📊 Final Metrics — Voltage: {metrics['voltage']}V, Temp: {metrics['temp']}C")
        log(f"⏱️ Test Duration: {t.duration:.2f}s")

        write_html_report(status, metrics, 1)
        export_metrics(metrics)
        log_result_csv(status, metrics)

        if not recovered:
            log(f"❌ {rack_id} failed recovery. Logging for analysis.")
