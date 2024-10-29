# from datetime import date

class Reading:
    # reading_date: date
    reading_date: str
    meter_reading: str

    def __init__(self, reading_date: str, meter_reading: str) -> None:
        # if not isinstance(reading_date, date):
        #     raise TypeError("Expected a datetime argument")
        # if not isinstance(meter_reading, str):
        #     raise TypeError("Expected a string argument")
        self.reading_date = reading_date
        self.meter_reading = meter_reading

    def __repr__(self) -> str:
        return f"Reading('{self.reading_date}', '{self.meter_reading}')"
