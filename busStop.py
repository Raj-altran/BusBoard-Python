# Bus stop class. Characterises the bus stop and lists it's departures.
from bus import Bus


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

    def __init__(self, dict):
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

    def printout_departures(self, cutoff):
        print(f"--{self.__name}--")
        for bus in self.__departures[:cutoff]:
            bus.printout()
        if self.__departures == []:
            print("No scheduled busses found")
        print("-"*20)

    def sort_departures(self):
        self.__departures.sort(key=lambda bus: bus.get_time())

