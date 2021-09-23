from flask import Flask, render_template, request
from postcode import Postcode
from constants import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/busInfo")
def busInfo():
    stop_num = request.args.get('stop_num')
    bus_num = request.args.get('bus_num')
    postcode = Postcode(request.args.get('postcode'), int(stop_num), int(bus_num))
    bus_stops = postcode.get_bus_stops()
    lat_longs = postcode.get_lat_longs()

    return render_template('info.html', postcode=postcode, bus_stops=bus_stops, lat_longs=lat_longs, KEY=GOOGLE_KEY_other)


if __name__ == "__main__": app.run()
