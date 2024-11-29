from Rental import Rental
from datetime import datetime, timedelta

class DataLoader:
    
    def __init__(self, rental):
        self.rental = rental
    
    def load(self):     
        self.rental.add_truck("AA-AA-01", "Renault", "Master Maxi", 20000, "480*180*205", 1200 )
        self.rental.add_car("AA-AA-02", "Opel", "Astra", 6000, "Szedán")
        self.rental.add_car("AA-AA-03", "Mitsubishi", "Colt", 8000, "Kombi")
        self.rental.add_rent(0, datetime(2024, 11, 1), datetime(2024, 11, 2))
        self.rental.add_rent(1, datetime(2024, 11, 6), datetime(2024, 11, 7))
        self.rental.add_rent(1, datetime(2024, 11, 24), datetime(2024, 11, 25))
        self.rental.add_rent(2, datetime(2024, 12, 8), datetime(2024, 12, 9))