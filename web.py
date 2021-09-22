from flask import Flask, render_template, request

from busStop import BusStop
# from dataVeiwerWeb import *
from postcode import Postcode
from requesters import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/busInfo")
def busInfo():
    postcode = Postcode(request.args.get('postcode'))
    if postcode.is_empty():
        bus_stops = {"Postcode not recognised": [["-", "-", "-"]]}
    else:
        bus_stops = postcode.get_bus_stops()

    return render_template('info.html', postcode=postcode, bus_stops=bus_stops)


if __name__ == "__main__": app.run()
