import datetime

class ParkingTicket:
    def __init__(self, ticket_no, level, spot, vehicle) -> None:
        self.ticket_no = ticket_no
        self.entry_time = 1
        self.level = level
        self.spot = spot 
        self.vehicle = vehicle