class Place:
    def __init__(self, address, district, neighborhood):
        self._address = address
        self._district = district
        self._neighborhood = neighborhood

    def to_string(self):
        return f"Address: {self._address}, District: {self._district}, Neighborhood: {self._neighborhood}"
