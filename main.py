from busStop import BusStop
from requesters import *
import web
from flask import Flask, render_template, request


def main():
    # app = Flask(__name__)
    # app.run()

    live = True
    while live:
        user_input = input("Enter a postcode: ")
        if user_input == "quit":
            live = False
            break
        elif user_input == "test":
            bus_ids = TEST_ATCOCODES
        elif user_input == "":
            bus_ids = ["0180BAC30345"]
        else:
            lat, long = postcode_to_LatLong(user_input)
            atcocodes = latLong_to_Atcocodes(lat, long)
            bus_ids = atcocodes

        for bus_id in range(len(bus_ids)):
            request = "Error"
            try:
                request = request_bus_stop(bus_ids[bus_id])
                bus_stop = BusStop(request)
                bus_stop.sort_departures()
                bus_stop.printout_departures(5)
            except KeyError:
                print_error(request)


def print_error(json):
    if "error" in json:
        print(json["error"])
    else:
        print("Bad input, try again.")
    print("-" * 20)


if __name__ == "__main__": main()
