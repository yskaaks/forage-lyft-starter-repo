from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear)

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3
