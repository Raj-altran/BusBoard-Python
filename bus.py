# bus departure class. characterises the event of a bus departing a stop.
from datetime import datetime


class Bus():
    __mode = "bus"
    __line = "68"
    __line_name = "68"
    __direction = "West Norwood"
    __operator = "ABLO"
    __date_aimed = datetime(1990, 1, 1)
    __date_expected = datetime(1990, 1, 1)

    def __init__(self, dict):
        self.__mode = dict["mode"]
        self.__line = dict["line"]
        self.__line_name = dict["line_name"]
        self.__direction = dict["direction"]
        self.__operator = dict["operator"]
        date = dict["date"].split('-')
        time_aimed = dict["aimed_departure_time"].split(":")
        time_expected = dict["expected_departure_time"].split(":")
        self.__date_aimed = datetime(int(date[0]), int(date[1]), int(date[2]),
                                     int(time_aimed[0]), int(time_aimed[1]), 0)
        self.__date_expected = datetime(int(date[0]), int(date[1]), int(date[2]),
                                        int(time_expected[0]), int(time_expected[1]), 0)

    def printout(self):
        output = f"{self.__line} {self.__mode} \t {self.__direction} \t {self.__date_expected.strftime('%H:%M')}"
        print(output)

    def get_time(self):
        return self.__date_expected
