
from framework.automation.stress_rack_controller import StressRackController
from framework.test_cases.mock_system_check import check_system_alive
from framework.utils.logger import log
from framework.utils.data_collector import collect_metrics
from framework.utils.report_writer import write_html_report

def test_power_cycle_recovery(max_retries=3):
    log("🚀 Starting power cycle recovery test...")
    try:
        rack = StressRackController("Rack-3")
        rack.power_cycle()

        log("📊 Collecting metrics...")
        metrics = collect_metrics()
        assert isinstance(metrics['voltage'], (int, float)) and isinstance(metrics['temp'], (int, float)), "Invalid metric types"
        log(f"⚡ Voltage: {metrics['voltage']}V, 🌡️ Temp: {metrics['temp']}C")

        for attempt in range(1, max_retries + 1):
            log(f"🔄 Attempt {attempt}: Checking system health...")
            if check_system_alive():
                log("✅ System recovered successfully.")
                write_html_report("PASS", metrics, attempt)
                return
            else:
                log("⚠️ System unresponsive. Retrying...")

        log("❌ System failed to recover after max retries.")
        write_html_report("FAIL", metrics, max_retries)
        raise AssertionError("System did not recover after power cycle")

    except Exception as e:
        log(f"🔥 Test encountered an error: {str(e)}")
        write_html_report("ERROR", {"voltage": "N/A", "temp": "N/A"}, 0, error=str(e))
        raise
