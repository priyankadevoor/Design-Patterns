"""
Req-
1. Only one entrance and one exit.

Entities - 
1. Vehicle
    - Enum CAR, MOTORCYCLE, TRUCK (Different cost)
    - Attributes:
        - License_plate
        - Vehicle_type
        - ticket
2. Levels 
    - Attributes:
        - level_no
        - No of parking spots which creates list of Parking Spots
    - Methods:
        - Park_car(Vehicle)
        - Unpark_car(Vehicle)
3. Parking Spot 
    - Attributes:
        - Spot_no
        - Spot_type [CAR, MOTORCYCLE, TRUCK] (Different cost)
        - available
        - price
    - Methods:
        - Park_car(Vehicle)
        - Unpark_car(Vehicle)
        - is_available()
4. Parking Lot
    - Attributes:
        - levels List of levels
    - Methods:
        - Park_car(Vehicle)
        - Unpark_car(Vehicle)
        - Add_Level
        - Get_nearest_available_spot()
        - is_full()
5. Ticket
    - Attributes:
        - ticket_no
        - entry_time
        - Vehicle
"""
from ParkingLevel import ParkingLevel
from ParkingTicket import ParkingTicket
from Vehicle import Car, Truck
import uuid

class ParkingLot:
    def __init__(self, number_of_levels, spots_per_level) -> None:
        self.levels = [ParkingLevel(i, spots_per_level) for i in range(number_of_levels)]
        self.total_spots = spots_per_level * number_of_levels
        self.total_free_spots = self.total_spots
    
    def is_full(self):
        if self.total_free_spots == 0:
            return True
        return False
    
    def park_vehicle(self, vehicle):
        if self.is_full():
            return 'Parking Lot is FULL!!'
        for level in self.levels:
            spot = level.get_available_spot(vehicle.get_vehicle_type())
            if spot:
                break
        ticket = ParkingTicket(uuid.uuid4(), level, spot, vehicle)
        spot.park_vehicle(vehicle)
        self.total_free_spots -= 1
        print(self.total_free_spots)
        return ticket
    
    def unpark_vehicle(self, ticket):
        time = 2 - ticket.entry_time
        spot = ticket.spot
        spot_price = ticket.spot.get_price()
        cost = time * spot_price
        spot.unpark_vehicle(ticket.vehicle)
        self.total_free_spots += 1
        print(self.total_free_spots)
        return cost

parking_lot = ParkingLot(2, 10)
car = Car('KA-09P-3620')
ticket = parking_lot.park_vehicle(car)
parking_lot.unpark_vehicle(ticket)

