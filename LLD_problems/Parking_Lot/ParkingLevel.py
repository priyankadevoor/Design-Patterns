from ParkingSpot import CarParkingSpot, CycleParkingSpot, TruckParkingSpot
from Vehicle import Car

class ParkingLevel:
    def __init__(self, level_no, no_of_spots):
        self.level_no = level_no
        self.no_of_spots = no_of_spots
        self._list_of_car_spots = [CarParkingSpot('car'+str(i)) for i in range(self.no_of_spots)]
        self._list_of_cycle_spots = [CycleParkingSpot('cycle'+str(i)) for i in range(self.no_of_spots)]
        self._list_of_truck_spots = [TruckParkingSpot('truck'+str(i)) for i in range(self.no_of_spots)]
    
    def get_available_spot(self, spot_type):
        if spot_type == 'VehicleType.CAR':
            for spot in self._list_of_car_spots:
                if spot.is_available():
                    return spot
        elif spot_type == 'VehicleType.MOTORCYCLE':
            for spot in self._list_of_cycle_spots:
                if spot.is_available():
                    return spot
        else:
            for spot in self._list_of_truck_spots:
                if spot.is_available():
                    return spot
                
