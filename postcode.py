from requesters import *
from busStop import BusStop


class Postcode:
    __code = "AA1 1AA"
    __lat = "0"
    __long = "0"
    __bus_stops = []
    __bus_limit=5

    def __init__(self, postcode, stop_num=2, bus_num=5):
        self.__code = postcode
        self.__lat, self.__long = postcode_to_LatLong(postcode)

        self.__bus_stops = []
        atcocodes = latLong_to_Atcocodes(self.__lat, self.__long, stop_num)
        for code in atcocodes:
            bus_stop = BusStop(code)
            bus_stop.sort_departures()
            self.__bus_stops.append(bus_stop)

        self.__bus_limit = bus_num

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
                output[(stop.get_name())] = stop.num_dir_time(self.__bus_limit)
        return output

    def get_lat_longs(self):
        output = []
        for stop in self.__bus_stops:
            output.append(stop.get_lat_long())
        return output
