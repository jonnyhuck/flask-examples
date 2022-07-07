from json import dumps
from shapely.geometry import LineString, mapping
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/route")
def hello_world():
    """
    * This is the web service that returns your route data
    *
    * An example call to this service would be:
    *   http://127.0.0.1:5000/route?from_lng=-2.807007&from_lat=54.065836&to_lng=-1.554565&to_lat=53.781181
    """
    
    # this is how you get the coords that were passed in
    from_lng = float(request.args['from_lng'])
    from_lat = float(request.args['from_lat'])
    to_lng = float(request.args['to_lng'])
    to_lat = float(request.args['to_lat'])

    # here I make them into a LineString - obviously wyou will output this from a route calculation...
    line_string = LineString([[from_lng, from_lat], [to_lng, to_lat]])

    # this is converting it from Python object to a GeoJSON string and returning it
    return dumps(mapping(line_string))

@app.route("/")
@app.route("/map")
def map():
    """
    * This is the web page that gets the route data
    """
    return render_template('./map.html')