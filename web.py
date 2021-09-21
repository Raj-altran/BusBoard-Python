from flask import Flask, render_template, request

from busStop import BusStop
from dataVeiwerWeb import *
from requesters import *

app = Flask(__name__)
viewer = DataViewerWeb()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/busInfo")
def busInfo():
    postcode = request.args.get('postcode')
    atcocodes = postcode_to_atcocodes(postcode)

    viewer.reset_bus_stops()
    for code in atcocodes:
        data = request_bus_stop(code)
        viewer.add_bus_stop(BusStop(data))

    bus_stops = viewer.get_stops()
    return render_template('info.html', postcode=postcode, bus_stops=bus_stops)


if __name__ == "__main__": app.run()
