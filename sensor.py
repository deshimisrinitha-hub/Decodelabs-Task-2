import random
import time

class Sensor:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0

    def read_sensor(self):
        self.temperature = round(random.uniform(20,40),2)
        self.humidity = round(random.uniform(40,80),2)

        return {
            "Temperature": self.temperature,
            "Humidity": self.humidity
        }