# dependencies
import datetime as dt
import numpy as np
import pandas as pd

# dependencies for SQLalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# dependencies for flask
from flask import Flask, jsonify

# key in ignition for engine for sqlite db
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# setup variables from Base class
# tsvar = Base.classes.keys()
# print("ok",tsvar)
Measurement = Base.classes.measurement
Station = Base.classes.station
###########################################################################py
# start engine
session = Session(engine)

# Flask app setup
app = Flask(__name__)

#create the home or root route
# Welcome, Precipitation, Stations, Monthly Temperature, and Statistics
@app.route('/')
def welcome():
    return(
        f'...<br/>'
        f'Welcome to the Climate Analysis API!<br/>'
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/temp/start/end<br/>'
        f'...'
    )

# setup the precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# set up the stations route
@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify (stations=stations)

# setup the monthly temp route
@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# setup the statistics route and use np library and start/end date
# @app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None,end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).\
        filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        # return temps
        return jsonify(temps=temps)
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    # return temps
    return jsonify(temps)
    
if __name__ == "__main__":
    app.run(debug=True)




