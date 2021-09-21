# DataViewerWeb class is used to output data via web
from flask import Flask, render_template, request


class DataViewerWeb:
    __postcode = "HU5 7RU"
    __bus_stops = []

    def __init__(self):
        self.__bus_stops = []

    def set_bus_stops(self, departures):
        self.__bus_stops = []

        for bus in departures:
            self.__bus_stops.append(bus.get_out())
        if not self.__departures:
            self.__bus_stops.append("No scheduled busses found")

    def add_bus_stop(self, bus_stop):
        self.__bus_stops.append(bus_stop)

    def reset_bus_stops(self):
        self.__bus_stops = []

    def get_stops(self):
        output = []
        for stop in self.__bus_stops:
            lines = stop.getout_departures()
            output.extend(lines)

        return output
