from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self):
        self.last_service_mileage = 0
        self.current_mileage = 0

    def needs_service(self):
        return True