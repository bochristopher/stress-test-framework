
class MockHAL:
    def power_on(self):
        print("Power ON (mock)")

    def power_off(self):
        print("Power OFF (mock)")

    def read_temp(self):
        return 42.0
