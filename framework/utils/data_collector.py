
import random

def collect_metrics():
    voltage = round(random.uniform(3.2, 3.4), 2)
    temp = round(random.uniform(40.0, 45.0), 1)
    return {
        "voltage": voltage,
        "temp": temp
    }
