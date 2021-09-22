import requests
from constants import *


def request_bus_stop(id):
    r = requests.get(
        f'https://transportapi.com/v3/uk/bus/stop/{id}/live.json?app_id={APP_ID}&app_key={APP_KEY}&group=route&nextbuses=yes')
    return r.json()


def postcode_to_LatLong(post_code):
    post_code = post_code.replace(" ", "")
    r = requests.get(f"http://api.postcodes.io/postcodes?q={post_code}")
    data = r.json()
    if data["result"] is None:
        return None, None
    else:
        lat = data["result"][0]["latitude"]
        long = data["result"][0]["longitude"]
        return lat, long


def latLong_to_Atcocodes(lat, long, limit=2):
    r = requests.get(
        f"http://transportapi.com/v3/uk/places.json?app_id={APP_ID}&app_key={APP_KEY}&lat={lat}&lon={long}&type=bus_stop")
    data = r.json()

    output = []
    if "error" in data:
        print("input error")
        print(data["error"])
        print("-" * 20)
    else:
        bus_stops = data["member"]
        for stop in bus_stops:
            atcocode = stop["atcocode"]
            output.append(atcocode)
    return output[:limit]


def postcode_to_atcocodes(postcode):
    if postcode == "":
        return []
    lat, long = postcode_to_LatLong(postcode)
    return latLong_to_Atcocodes(lat, long)


def print_error(json):
    if "error" in json:
        print(json["error"])
    else:
        print("Bad input, try again.")
    print("-" * 20)
