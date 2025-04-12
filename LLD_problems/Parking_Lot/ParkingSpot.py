"""3. Parking Spot 
    - Attributes:
        - Spot_no
        - Spot_type [CAR, MOTORCYCLE, TRUCK] (Different cost)
        - available
        - price
    - Methods:
        - Park_car(Vehicle)
        - Unpark_car(Vehicle)
        - is_available()"""




from enum import Enum

class SpotType(Enum):
    CAR = 1 
    CYCLE = 2
    TRUCK = 3

class ParkingSpot:
    def __init__(self, spot_number):
        self._spot_number = spot_number
        self._available = True
        self._parked_vehicle = None
    def get_price(self):
        pass
    def get_spot_type(self):
        pass
    def is_available(self):
        return self._available
    def get_spot_number(self):
        return self._spot_number
    def get_parked_vehicle(self):
        return self._parked_vehicle
    def park_vehicle(self, vehicle):
        if self.is_available():
            self._parked_vehicle = vehicle
            self._available = False
            return True
        return False
    def unpark_vehicle(self, vehicle):
        if self.is_available() and self.parked_vehicle == vehicle:
            self._parked_vehicle = None
            self._available = True
            return True
        return False
        
class CarParkingSpot(ParkingSpot):
    def get_price(self):
        return 20
    def get_spot_type(self):
        return SpotType.CAR

class CycleParkingSpot(ParkingSpot):
    def get_price(self):
        return 10
    def get_spot_type(self):
        return SpotType.CYCLE
    
class TruckParkingSpot(ParkingSpot):
    def get_price(self):
        return 25
    def get_spot_type(self):
        return SpotType.TRUCK
    

