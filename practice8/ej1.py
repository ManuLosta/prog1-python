class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometers = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.brand} {self.model}"

    def read_odometer(self):
        return f"This car has {self.kilometers} kilometers on it."

    def update_odometer(self, new_kilometers):
        if new_kilometers > self.kilometers:
            self.kilometers = new_kilometers
    
    def increment_odometer(self, increment):
        self.kilometers += increment

