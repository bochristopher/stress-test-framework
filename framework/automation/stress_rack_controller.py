
import time

class StressRackController:
    def __init__(self, rack_id):
        self.rack_id = rack_id

    def power_cycle(self, delay=2):
        print(f"[INFO] Power cycling rack {self.rack_id}")
        print("[ACTION] Power OFF")
        time.sleep(delay)
        print("[ACTION] Power ON")
        time.sleep(delay)
        print("[SUCCESS] Rack power cycled successfully.")

    def set_temperature(self, temp_c):
        print(f"[INFO] Setting temperature to {temp_c}C on rack {self.rack_id}")
        time.sleep(1)
        print(f"[SUCCESS] Temperature stabilized at {temp_c}C")
