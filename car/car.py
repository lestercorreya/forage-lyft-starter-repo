from serviceable.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
