class Car:
    def __init__(self, make, model, year):
        self.make = make          # Attribute
        self.model = model        # Attribute
        self.year = year          # Attribute
    
    def start_engine(self):       # Method
        print(f"{self.year} {self.make} {self.model} engine started.")