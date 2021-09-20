import requests
from busStop import BusStop
from constants import *


def main():
    print("Welcome to BusBoard.")

    live = True
    while live:
        user_input = input("Enter a atco code: ")
        if user_input == "quit":
            live = False
            break
        elif user_input == "":
            bus_id = "0180BAC30345"
        else:
            bus_id = user_input

        try:
            request = request_bus_stop(bus_id)
            busstop = BusStop(request)
            busstop.sort_departures()
            busstop.printout_departures()
        except KeyError:
            print("Bad input, try again.")


def request_bus_stop(id):
    r = requests.get(
        f'https://transportapi.com/v3/uk/bus/stop/{id}/live.json?app_id={APP_ID}&app_key={APP_KEY}&group=route&nextbuses=yes')
    return r.json()


if __name__ == "__main__": main()
