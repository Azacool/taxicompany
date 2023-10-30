from place import Place
from passenger import Passenger
from taxi import Taxi
from taxi_company import TaxiCompany
from exceptions import InvalidTaxiName
from trip import Trip

pickup_place = Place("Al-khorazmiy 9 St", "Chilonzor", "Borijar Mahallasi")
destination_place = Place("Furqat St", "Chilonzor", "Khirmontepa Mahallasi")

passenger = Passenger(pickup_place)
taxi1 = Taxi(1)
taxi2 = Taxi(2)
#taxi3 = Taxi(1)

company = TaxiCompany()
company.add_taxi(taxi1)
company.add_taxi(taxi2)
#company.add_taxi(taxi3)

my_taxi = company.call_taxi(passenger)
if my_taxi:
        print(f"Taxi {my_taxi._unique_id} called for passenger pickup")

        print(my_taxi.begin_trip(destination_place))

        print(my_taxi.terminate_trip())

        print(f"Lost trips: {company.get_lost_trips()}")

        
        trips = company.get_trips(1)
        print(f"Trips for Taxi 1: {trips}")
        
else:
    print("No available taxis. Call canceled.")
