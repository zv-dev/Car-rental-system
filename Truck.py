from Vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, id, license_plate_number, brand, vehicle_type, rental_fee, cargo_space, maximum_weight_loaded):
            self.cargo_space = cargo_space
            self.maximum_weight_loaded = maximum_weight_loaded
            super().__init__(id, license_plate_number, brand, vehicle_type, rental_fee)

    def get_data_sheet(self):
            return {
            'Azonosító': self.id,
            'Rendszám': self.license_plate_number,
            'Modell': self.brand,
            'Típus': self.vehicle_type,
            'Bérlési díj': self.rental_fee,
            'Raktér méret': self.cargo_space,
            'Maximális terhelhetőség': self.maximum_weight_loaded
        }