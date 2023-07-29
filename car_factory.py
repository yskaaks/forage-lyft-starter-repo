from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery
from tire import CarriganTire, OctoprimeTire

class CarFactory:
    def create_car(self, car_type, **kwargs):
        if car_type == 'Calliope':
            return Car(CapuletEngine(**kwargs), SpindlerBattery(**kwargs), CarriganTire(**kwargs))
        elif car_type == 'Glissade':
            return Car(WilloughbyEngine(**kwargs), SpindlerBattery(**kwargs), CarriganTire(**kwargs))
        elif car_type == 'Palindrome':
            return Car(SternmanEngine(**kwargs), NubbinBattery(**kwargs), OctoprimeTire(**kwargs))
        elif car_type == 'Rorschach':
            return Car(WilloughbyEngine(**kwargs), NubbinBattery(**kwargs), OctoprimeTire(**kwargs))
        elif car_type == 'Thovex':
            return Car(CapuletEngine(**kwargs), NubbinBattery(**kwargs), CarriganTire(**kwargs))
        else:
            raise ValueError("Invalid car type")
