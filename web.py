from flask import Flask, render_template, request
from postcode import Postcode

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/busInfo")
def busInfo():
    postcode = Postcode(request.args.get('postcode'))
    bus_stops = postcode.get_bus_stops()
    lat_longs = postcode.get_lat_longs()

    return render_template('info.html', postcode=postcode, bus_stops=bus_stops, lat_longs=lat_longs)


if __name__ == "__main__": app.run()
