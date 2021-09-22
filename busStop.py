# Bus stop class. Characterises the bus stop and lists it's departures.
from bus import Bus
from requesters import request_bus_stop


class BusStop:
    __atcocode = "490000077E"
    __name = "Euston Station (Stop E)"
    __lat = "0"
    __long = "0"
    __departures = []

    def __init__(self, atcocode):
        dict = request_bus_stop(atcocode)

        self.__atcocode = dict["atcocode"]
        self.__name = dict["name"]

        self.__lat = dict["location"]["coordinates"][1]
        self.__long = dict["location"]["coordinates"][0]

        self.__departures = []
        for item in dict["departures"]:
            for busEvent in dict["departures"][item]:
                self.__departures.append(Bus(busEvent))

    def sort_departures(self):
        self.__departures.sort(key=lambda bus: bus.get_time())

    def num_dir_time(self):
        output = []
        for bus in self.__departures:
            output.append([bus.get_number(), bus.get_direction(), bus.get_time()])
        return output[:5]

    def get_name(self):
        return self.__name

    def get_lat_long(self):
        return {"lat":self.__lat, "lng":self.__long}