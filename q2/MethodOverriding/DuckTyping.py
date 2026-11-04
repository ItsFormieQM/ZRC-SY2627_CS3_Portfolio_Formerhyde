import wrappers as wrp
def start_trip(vehicle):
    try:
        vehicle.move()
    except AttributeError:
        wrp.sdm("error")
class Car:
    def move(self):
        wrp.sdm("The car drives on the road.")
class Boat:
    def move(self):
        wrp.sdm("The boat sails on water.")
class Drone:
    def move(self):
        wrp.sdm("The drone flies in the sky.")
obj = Car()
start_trip(obj)
obj = Boat()
start_trip(obj)
obj = Drone()
start_trip(obj)
