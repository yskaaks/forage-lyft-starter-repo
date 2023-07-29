import unittest
from tire import CarriganTire, OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service(self):
        tire = CarriganTire(tire_wear=[0.9, 0.8, 0.7, 0.6])
        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        tire = CarriganTire(tire_wear=[0.8, 0.7, 0.6, 0.5])
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service(self):
        tire = OctoprimeTire(tire_wear=[0.8, 0.8, 0.8, 0.8])
        self.assertTrue(tire.needs_service())

    def test_does_not_need_service(self):
        tire = OctoprimeTire(tire_wear=[0.7, 0.7, 0.7, 0.7])
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
