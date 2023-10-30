class InvalidTaxiName(Exception):
    def __init__(self, message="Invalid Taxi Name: Taxi with this ID already exists"):
        self.message = message
        super().__init__(self.message)
