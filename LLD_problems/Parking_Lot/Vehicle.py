from VehicleType import VehicleType

class Vehicle:
    def __init__(self, license_plate, vehicle_type) -> None:
        self._license_plate = license_plate
        self._vehicle_type = vehicle_type
        self._assigned_ticket = None
    
    def get_license_plate(self):
        return self._license_plate

    def get_vehicle_type(self):
        return self._vehicle_type

    
class Car(Vehicle):
    def __init__(self, license_plate) -> None:
        super().__init__(license_plate, VehicleType.CAR)

class Motorcycle(Vehicle):
    def __init__(self, license_plate) -> None:
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

class Truck(Vehicle):
    def __init__(self, license_plate) -> None:
        super().__init__(license_plate, VehicleType.TRUCK)
    

