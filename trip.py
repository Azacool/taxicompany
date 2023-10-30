class Trip:
    def __init__(self, start_address, end_address):
        self._start_address = start_address
        self._end_address = end_address

    def to_string(self):
        return f"{self._start_address.to_string()}, {self._end_address.to_string()}"

