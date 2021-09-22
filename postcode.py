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

        self.__bus_stops = []
        atcocodes = latLong_to_Atcocodes(self.__lat, self.__long)
        for code in atcocodes:
            bus_stop = BusStop(code)
            bus_stop.sort_departures()
            self.__bus_stops.append(bus_stop)

    def __str__(self):
        return self.__code

    def is_empty(self):
        return self.__bus_stops == []

    def get_bus_stops(self):
        output = {}
        if not self.__bus_stops:
            output = {"Postcode not recognised": [["-", "-", "-"]]}
        else:
            for stop in self.__bus_stops:
                output[(stop.get_name())] = stop.num_dir_time()
        return output

    def get_lat_longs(self):
        output = []
        for stop in self.__bus_stops:
            output.append(stop.get_lat_long())
        return output