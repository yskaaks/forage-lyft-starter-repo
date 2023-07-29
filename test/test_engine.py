import unittest
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = CapuletEngine(last_service_mileage=20000, current_mileage=51000)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        engine = CapuletEngine(last_service_mileage=20000, current_mileage=30000)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = WilloughbyEngine(last_service_mileage=20000, current_mileage=81000)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        engine = WilloughbyEngine(last_service_mileage=20000, current_mileage=60000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
