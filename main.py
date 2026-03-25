import logging
import time
from kostal_modbus import KostalModbus
from goe_charger import GoeCharger

# Configure logging
logging.basicConfig(level=logging.INFO)

class IntelligentPVCharging:
    def __init__(self):
        self.kostal_modbus = KostalModbus()
        self.goe_charger = GoeCharger()
        self.setup_logging()

    def setup_logging(self):
        logging.info("Starting Intelligent PV Charging orchestration...")

    def read_pv_data(self):
        pv_data = self.kostal_modbus.read_data()
        logging.debug(f"PV Data: {pv_data}")
        return pv_data

    def control_charger(self, pv_data):
        if pv_data['power'] > 0:
            logging.info("Sufficient PV power, enabling charger...")
            self.goe_charger.enable_charging()
        else:
            logging.info("Insufficient PV power, disabling charger...")
            self.goe_charger.disable_charging()

    def run(self):
        while True:
            pv_data = self.read_pv_data()
            self.control_charger(pv_data)
            time.sleep(60)  # Run every minute

if __name__ == '__main__':
    intelligent_charging = IntelligentPVCharging()
    intelligent_charging.run()