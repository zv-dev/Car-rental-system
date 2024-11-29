from Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, id, license_plate_number, brand, vehicle_type, rental_fee, design):
            self.design = design
            super().__init__(id, license_plate_number, brand, vehicle_type, rental_fee)
    
    def get_data_sheet(self):
            return {
            'Azonosító': self.id,
            'Rendszám': self.license_plate_number,
            'Modell': self.brand,
            'Típus': self.vehicle_type,
            'Bérlési díj': self.rental_fee,
            'Kivitel': self.design
        }    