from requesters import *
from busStop import BusStop


class Postcode:
    __code = "AA1 1AA"
    __lat = "0"
    __long = "0"
    __bus_stops = []

    def __init__(self, postcode):
        self.__code = postcode
        self.__lat, self.__long = postcode_to_LatLong(postcode)
        atcocodes = latLong_to_Atcocodes(self.__lat, self.__long)
        for code in atcocodes:
            self.__bus_stops.append(BusStop(code))

    def __str__(self):
        return self.__code

    def is_empty(self):
        return self.__bus_stops == []

    def get_bus_stops(self):
        output1 = {}
        for stop in self.__bus_stops:
            output1[(stop.get_name())] = stop.num_dir_time()
        return output1

