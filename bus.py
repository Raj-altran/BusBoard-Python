# bus departure class. characterises the event of a bus departing a stop.
from datetime import datetime


class Bus():
    __mode = "bus"
    __line = "68"
    __direction = "West Norwood"
    __datetime = datetime(1990, 1, 1)

    def __init__(self, dict):
        self.__mode = dict["mode"]
        self.__line = dict["line"]
        self.__direction = dict["direction"]

        time = "1900-01-01"
        if dict["expected_departure_time"] is not None:
            time = dict["date"].split('-') + dict["expected_departure_time"].split(":")
            time = [int(string) for string in time]
        elif dict["aimed_departure_time"] is not None:
            time = dict["date"].split('-') + (dict["aimed_departure_time"].split(":"))
            time = [int(string) for string in time]

        self.__datetime = datetime(time[0], time[1], time[2], time[3], time[4], 0)

    def get_number(self):
        return self.__line

    def get_direction(self):
        return self.__direction

    def get_time(self):
        return self.__datetime.strftime("%H:%M")
