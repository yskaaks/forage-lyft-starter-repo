import unittest
from datetime import datetime, timedelta
from battery import SpindlerBattery, NubbinBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        battery = SpindlerBattery(last_service_date=datetime.today() - timedelta(days=1096), current_date=datetime.today())
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        battery = SpindlerBattery(last_service_date=datetime.today() - timedelta(days=1094), current_date=datetime.today())
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        battery = NubbinBattery(last_service_date=datetime.today() - timedelta(days=731), current_date=datetime.today())
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        battery = NubbinBattery(last_service_date=datetime.today() - timedelta(days=729), current_date=datetime.today())
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
