from abc import ABC,abstractmethod
# from math import floor removed overhead
class Sensor(ABC):
    @abstractmethod
    def get_reading():
        pass

class PHSensor(Sensor):
    def get_reading(self):
        result = 9
        status = result
        # if result > 7:
        #     status = "Acidic"
        # elif floor(result) == 7:
        #     status = "Neutral"
        # elif result >= 8:
        #     status = "Basic"
        # else:
        #     raise "Exception Occurred"
        result = "[PH Sensor] Reading: "
        result += str(status) + "°C"
        return result
        pass
class TempSensor(Sensor):
    def get_reading(self):
        result = 24.5
       
        # if result > 7:
        #     status = "Acidic"
        # elif floor(result) == 7:
        #     status = "Neutral"
        # elif result >= 8:
        #     status = "Basic"
        # else:
        #     raise "Exception Occurred"
        return f"[Temperature Sensor] Reading: {result}°C"
print("--- Lab Inventory System ---")
obj_phsensor = PHSensor()
obj_tempsensor = TempSensor()
print(obj_phsensor.get_reading())
print(obj_tempsensor.get_reading())
try:
    mysensor = Sensor()
except TypeError:
    print("Error")