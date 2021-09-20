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

        time_aimed = dict["date"].split('-') + (dict["aimed_departure_time"].split(":"))
        time_aimed = [int(string) for string in time_aimed]
        time_expected = dict["date"].split('-') + dict["expected_departure_time"].split(":")
        time_expected = [int(string) for string in time_expected]
        self.__date_aimed = datetime(time_aimed[0], time_aimed[1], time_aimed[2],
                                     time_aimed[3], time_aimed[4], 0)
        self.__date_expected = datetime(time_expected[0], time_expected[1], time_expected[2],
                                        time_expected[3], time_expected[4], 0)

    def printout(self):
        destination = self.__direction+" "*20
        destination = destination[:20]

        output = f"{self.__line} {self.__mode} \t {destination} \t {self.__date_expected.strftime('%H:%M')}"
        print(output)

    def get_time(self):
        return self.__date_expected
