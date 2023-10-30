from place import Place  

class Passenger:
    def __init__(self, place:Place):
        self._place = place

    def get_place(self):
        return self._place.to_string()
