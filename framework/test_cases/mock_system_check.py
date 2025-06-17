
import random
import time

def check_system_alive():
    print("[INFO] Checking if system is alive...")
    time.sleep(1)
    result = random.choices([True, False], weights=[90, 10])[0]
    print(f"[RESULT] System status: {'Alive' if result else 'Unresponsive'}")
    return result
