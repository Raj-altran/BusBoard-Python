import requests
from busStop import BusStop
from constants import *


def main():
    print("Welcome to BusBoard.")

    bus_id = "0180BAC30345"

    r = requests.get(f'https://transportapi.com/v3/uk/bus/stop/{bus_id}/live.json?app_id={APP_ID}&app_key={APP_KEY}&group=route&nextbuses=yes')
    request = r.json()

    busstop = BusStop(request)
    busstop.sort_departures()

    busstop.printout_departures()


if __name__ == "__main__": main()