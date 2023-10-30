from place import Place
from trip import Trip
class Taxi:
    def __init__(self, unique_id):
        self._unique_id = unique_id
        self._is_busy=False
        self._passenger=None
        self._trips:list[Trip] = []

    def to_string(self):
        return f"Taxi ID: {self._unique_id}"
    

    def begin_trip(self, destination):
        if self._is_busy:
            return "Taxi is already occupied"
        else:
            self.passenger._place= destination
            self._is_busy = True
            return f"Trip started to {destination.to_string()}"

    def terminate_trip(self):
        if self._is_busy:
            self._is_busy = False
            self.passenger = None
            return "Trip terminated"
        else:
            return "No trip in progress"
        
    def get_trips(self):
        return [trip.to_string() for trip in self._trips]
        