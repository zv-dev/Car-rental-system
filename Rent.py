from datetime import datetime, timedelta

class Rent:

    def __init__(self, id, vehicle, start_date, end_date):
        self.id = id
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.deleted = False

    def get_rent(self, only_live = False):
        msgdict = {
            'Azonosító': self.id,
            'Jármű azonosító': self.vehicle.get_id(),
            'Bérlés kezdő dátuma': self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            'Bérlés vége': self.end_date.strftime("%Y-%m-%d %H:%M:%S"),
        }
        if not only_live:
            msgdict['Törölve'] = self.deleted
        return msgdict       
    
    def get_live_rent(self):
        if(not self.deleted):
            return self.get_rent(True)
    
    def get_current_rent(self):
        if(self.start_date >= datetime.today() and not self.deleted):
            return self.get_rent(True)

    def is_rent_completed(self):
        return self.end_date <= datetime.today() and not self.deleted
    
    def is_rented(self, vehicle_id, start_date, end_date):
        return (vehicle_id == self.vehicle.get_id() and self.deleted == False and (
            start_date <= self.start_date and end_date >= self.start_date 
            or 
            start_date <= self.end_date and end_date >= self.end_date
            or
            start_date >= self.start_date and end_date <= self.end_date
            or
            start_date <= self.start_date and end_date >= self.end_date))
        
    def delete_rent(self):
        self.deleted = True