from datetime import datetime
from battery.battery import Battery

class NubbinBatter(Battery):
    def __init__(self):
        self.last_service_date = datetime.today().date()
        self.current_date = datetime.today().date()

    def needs_service():
        pass