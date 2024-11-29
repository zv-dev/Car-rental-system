from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, id, license_plate_number, brand, vehicle_type, rental_fee):
        self.id = id
        self.license_plate_number = license_plate_number
        self.brand = brand
        self.vehicle_type = vehicle_type
        self.rental_fee = rental_fee
        self.is_rented = False

    @abstractmethod
    def get_data_sheet(self):
        pass

    def get_id (self):
        return self.id
    
    def get_rental_fee (self):
        return self.rental_fee

    