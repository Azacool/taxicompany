from taxi import Taxi
from exceptions import InvalidTaxiName
from trip import Trip

class TaxiCompany:
    def __init__(self):
        self.taxi_list:list[Taxi]= []
        self._lost_trips = 0 

    def add_taxi(self, taxi:Taxi):
        for t in self.taxi_list:
            if t._unique_id == taxi._unique_id:
                raise InvalidTaxiName
        self.taxi_list.append(taxi)

    def get_available(self):
        return [taxi.to_string() for taxi in self.taxi_list]
    
 
    def call_taxi(self, passenger):
        for taxi in self.taxi_list:
            if not taxi._is_busy:
                taxi.passenger = passenger
                return taxi
        self._lost_trips += 1
        return None

    def get_lost_trips(self):
        return self._lost_trips

    def get_trips(self, taxi_id):
        for taxi in self.taxi_list:
            if taxi._unique_id == taxi_id:
                return taxi.get_trips()
        raise InvalidTaxiName("Taxi not found")










     