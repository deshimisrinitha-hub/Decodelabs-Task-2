from sensor import Sensor
import time

sensor = Sensor()

print("Sensor Simulation Started")

while True:
    data = sensor.read_sensor()

    print("----------------")
    print("Sensor Data")
    print("Temperature:", data["Temperature"], "°C")
    print("Humidity:", data["Humidity"], "%")

    time.sleep(2)