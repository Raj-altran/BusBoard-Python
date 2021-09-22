# Bus stop class. Characterises the bus stop and lists it's departures.
from bus import Bus
from requesters import request_bus_stop


class BusStop:
    __atcocode = "490000077E"
    __smscode = "58234"
    __name = "Euston Station (Stop E)"
    __stop_name = "Euston Station"
    __bearing = "E"
    __indicator = "Stop E"
    __locality = "Euston, London"
    __location = {
        "type": "Point",
        "coordinates": [
            -0.1317,
            51.52776
        ]
    }
    __departures = []

    def __init__(self, atcocode):
        dict = request_bus_stop(atcocode)

        self.__atcocode = dict["atcocode"]
        self.__smscode = dict["smscode"]
        self.__name = dict["name"]
        self.__stop_name = dict["stop_name"]
        self.__bearing = dict["bearing"]
        self.__indicator = dict["indicator"]
        self.__locality = dict["locality"]
        self.__location = dict["location"]
        self.__departures = []

        for item in dict["departures"]:
            for busEvent in dict["departures"][item]:
                self.__departures.append(Bus(busEvent))

    def printout_departures(self, cutoff=5):
        print(f"--{self.__name}--")
        for bus in self.__departures[:cutoff]:
            bus.printout()
        if not self.__departures:
            print("No scheduled busses found")
        print("-" * 20)

    def getout_departures(self, cutoff=5):
        output = [f"--{self.__name}--"]
        for bus in self.__departures[:cutoff]:
            output.append(bus.getout())
        if not self.__departures:
            output.append("No scheduled busses found")
        output.append("-" * 20)

        return output

    def sort_departures(self):
        self.__departures.sort(key=lambda bus: bus.get_time())

    def num_dir_time(self):
        output = []
        for bus in self.__departures:
            output.append([bus.get_number(), bus.get_direction(), bus.get_time()])
        return output

    def get_name(self):
        return self.__name
