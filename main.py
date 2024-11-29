from Truck import Truck
from Car import Car
from Rental import Rental
from Rent import Rent
from datetime import datetime, timedelta
from ConsoleWriter import ConsoleWriter
from DataLoader import DataLoader

class RentalSystem:

    def __init__(self):
        
        self.rental = Rental("Autókölcsönző", ConsoleWriter())
        self.loader = DataLoader(self.rental)
        self.loader.load()

    def user_interact(self):
        while True:
            print("1. Járművek listázása")
            print("2. Összes bérlés listázása")
            print("3. Élő (nem törölt) bérlések listázása")
            print("4. Aktuális bérlések listázása")
            print("5. Járművek bérlése")
            print("6. Járműbérlés lemondása")
            print("7. Kilépés")

            menu = input("Válassz a fenti menüpontokból: ")

            if menu == "1":
                print('Elérhető járművek:')
                self.rental.print_vehicles()
            elif menu == "2":
                print('Összes bérlés:')
                self.rental.print_rents()
            elif menu == "3":
                print('Élő (nem törölt) bérlések:')
                self.rental.print_live_rents()
            elif menu == "4":
                print('Aktuális bérlések:')
                self.rental.print_current_rents()
            elif menu == "5":
                print('Először adja meg a bérlés időintervallumát az elérhető autók kilistázásához!')
                while True:
                    while True:
                        start_date_input = input("Bérlés kezdő dátuma: ")
                        try:
                            start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
                            if (start_date < datetime.today()):
                                print('A kezdő dátum nem lehet korábbi, mint a holnapi dátum!')
                            else:
                                break
                        except:
                            print('Nem megfelelő kezdő dátum, használja a "Y-m-d" formátumot!')
                    
                    while True:
                        end_date_input = input("Bérlés végének dátuma: ")
                        try:
                            end_date = datetime.strptime(end_date_input, "%Y-%m-%d")
                            break
                        except:
                            print('Nem megfelelő vég dátum, használja a "Y-m-d" formátumot!')

                    if(start_date > end_date):
                        print('A kezdő dátumnak korábbinak kell lennie, mint a befejezés dátuma!')
                    else:
                        if(end_date - start_date > timedelta(days=1) ):
                            print('A bérlés időtartama csak 1 nap lehet!')
                        else:
                            print('A megadott időintervallumban elérhető járművek:')
                            avaiable_vehice_ids = self.rental.get_available_vehicles(start_date, end_date)
                            if len(avaiable_vehice_ids) == 0:
                                print('A megadott időszakban egyetlen gépjármű sem elérhető!')
                            else:
                                break
                while True:
                    text = input("Kérem adja meg a kiválasztott gépjármű azonosítóját: ")
                    if(not text.isnumeric()):
                        print('A jármű azonosító csak szám lehet!')
                    else:
                        id = int(text)
                        if not (self.rental.check_vehicle_exist(id)):
                            print('Nem létező jármű azonosítót adott meg, kérem adjon meg egy másik azonosító számot!')
                        else:
                            if(id not in avaiable_vehice_ids):
                                print('A megadott azonosítójú gépjarmű nem szabad!')
                            else:
                                break
                rent = self.rental.add_rent(id, start_date, end_date)
                print(f"Gépjármű kibérelve!")
                print(f"Bérlés azonosítója: {rent.id}")
                print(f"Gépjármű azonosítója: {id}")
                print(f"Kezdő időpont: {start_date}")
                print(f"Záró időpont: {end_date}")
                print(f"Fizetendő: {rent.vehicle.get_rental_fee()} Ft.")
            elif menu == "6":
                while True:
                    text_rent = (input("Addja meg a bérlés azonosítót: "))
                    if(not text_rent.isnumeric()):
                        print('A bérlés azonosító csak szám lehet!')
                    else:
                        id = int(text_rent)
                        if not self.rental.check_rent_exist(id):
                            print('Nem létező bérlés azonosítót adott meg, kérem adjon meg egy másik azonosító számot!')
                        else:
                            if self.rental.is_rent_completed(id):
                                print('Teljesített bérlés nem törölhető!')
                            else:
                                break
                self.rental.cancel_rent_by_id(id)
                print(f"A {id} azonosítójú bérlés lemondásra került.")
            elif menu == "7":
                break

rental_system = RentalSystem()
rental_system.user_interact()