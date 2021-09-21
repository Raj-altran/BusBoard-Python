from busStop import BusStop
from requesters import *
from dataVeiwerWeb import *
from web import *
from flask import Flask, render_template, request


def main():
    app.run()

    # live = True
    # while live:
    #     user_input = input("Enter a postcode: ")
    #     if user_input == "quit":
    #         live = False
    #         break
    #     elif user_input == "test":
    #         bus_ids = TEST_ATCOCODES
    #     else:
    #         bus_ids = postcode_to_atcocodes(user_input)
    #
    #     for bus_id in range(len(bus_ids)):
    #         request = "Error"
    #         try:
    #             request = request_bus_stop(bus_ids[bus_id])
    #             bus_stop = BusStop(request)
    #             bus_stop.sort_departures()
    #             bus_stop.printout_departures(5)
    #         except KeyError:
    #             print_error(request)


if __name__ == "__main__": main()
