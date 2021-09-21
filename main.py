import requests
from busStop import BusStop
from constants import *


def main():
    print("Welcome to BusBoard.")

    live = True
    while live:
        user_input = input("Enter a postcode: ")
        if user_input == "quit":
            live = False
            break
        elif user_input == "test":
            bus_ids = ["0180BAC30345",
                       "0180BAC30342",
                       "0180BAC30601",
                       "0180BAC31197",
                       "0180BAC30587",
                       "0180BAZ02395",
                       "0180BAC30614"]
        elif user_input == "":
            bus_ids = ["0180BAC30345"]
        else:
            lat, long = postcode_to_LatLong(user_input)
            atcocodes = latLong_to_Atcocodes(lat, long)
            bus_ids = atcocodes

        for bus_id in range(len(bus_ids)):
            try:
                request = request_bus_stop(bus_ids[bus_id])
                bus_stop = BusStop(request)
                bus_stop.sort_departures()
                bus_stop.printout_departures(5)
            except KeyError:
                print_error(request)


def request_bus_stop(id):
    r = requests.get(
        f'https://transportapi.com/v3/uk/bus/stop/{id}/live.json?app_id={APP_ID}&app_key={APP_KEY}&group=route&nextbuses=yes')
    return r.json()


def print_error(json):
    if "error" in json:
        print(json["error"])
    else:
        print("Bad input, try again.")
    print("-" * 20)


def postcode_to_LatLong(post_code):
    post_code = post_code.replace(" ","")
    r = requests.get(f"http://api.postcodes.io/postcodes?q={post_code}")
    data = r.json()
    if data["result"] is None:
        return None, None
    else:
        lat = data["result"][0]["latitude"]
        long = data["result"][0]["longitude"]
        return lat, long


def latLong_to_Atcocodes(lat, long):
    r = requests.get(
        f"http://transportapi.com/v3/uk/places.json?app_id={APP_ID}&app_key={APP_KEY}&lat={lat}&lon={long}&type=bus_stop")
    data = r.json()

    output = []
    if "error" in data:
        print("input error")
        print(data["error"])
        print("-"*20)
    else:
        bus_stops = data["member"]
        for stop in bus_stops:
            atcocode = stop["atcocode"]
            output.append(atcocode)
    return output[:2]


if __name__ == "__main__": main()
