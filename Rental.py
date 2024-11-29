from datetime import datetime, timedelta
from Rent import Rent
from Truck import Truck
from Car import Car

class Rental:

    def __init__(self, name, writer):
        self._name = name
        self.vehicles = []
        self.rents = []
        self.writer = writer

    @property
    def name(self):
        return self._name

    def print_vehicles(self):
        messages = []
        for vehicle in self.vehicles:
            messages.append(vehicle.get_data_sheet())
        self.print_dict(messages)
    
    def get_available_vehicles(self, start_date, end_date):
        messages = []
        avaiable_vehice_ids = []
        for vehicle in self.vehicles:
            available = True
            for rent in self.rents:
                if rent.is_rented(vehicle.get_id(), start_date, end_date):
                    available = False
            if(available):
                avaiable_vehice_ids.append(vehicle.get_id())
                messages.append(vehicle.get_data_sheet())
        self.print_dict(messages)
        return avaiable_vehice_ids
        
    def add_truck(self, license_plate_number, brand, vehicle_type, rental_fee, cargo_space, maximum_weight_loaded):
        truck = Truck(len(self.vehicles), license_plate_number, brand, vehicle_type, rental_fee, cargo_space, maximum_weight_loaded)
        self.vehicles.append(truck)
        return truck
    
    def add_car(self, license_plate_number, brand, vehicle_type, rental_fee, design):
        car = Car(len(self.vehicles), license_plate_number, brand, vehicle_type, rental_fee, design)
        self.vehicles.append(car)
        return car

    def check_vehicle_exist(self, id):
        try:
            return self.vehicles[id]
        except:
            return False
        
    def check_rent_exist(self, id):
        try:
            return self.rents[id]
        except:
            return False

    def is_rent_completed(self, id):
        return self.rents[id].is_rent_completed()

    def print_rents(self):
        messages = []
        for rent in self.rents:
            messages.append(rent.get_rent())
        self.print_dict(messages)

    def print_current_rents(self):
        messages = []
        for rent in self.rents:
            messages.append(rent.get_current_rent())
        self.print_dict(messages)
    
    def print_live_rents(self):
        messages = []
        for rent in self.rents:
            messages.append(rent.get_live_rent())
        self.print_dict(messages)

    def add_rent(self, vehicle_id, start_date, end_date):
        rent = Rent(len(self.rents), self.vehicles[vehicle_id], start_date, end_date)
        self.rents.append(rent)
        return rent

    def get_rents_length(self):
        return len(self.rents)

    def cancel_rent_by_id(self, rent_id):
        self.rents[rent_id].delete_rent()
        
    def print_dict(self, msg):
        self.writer.print(msg)

