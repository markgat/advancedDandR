from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Planning for Hawaii? <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"Start date given:<br/>"
        f"/api/v1.0/YYYY-MM-DD<br/><br/>"
        f"Start and end dates<br/>"
        f"//api/v1.0/YYYY-MM-DD/YYYY-MM-DD"
        )
@app.route("/api/v1.0/precipitation")
def rain():
    pre_json ={}
    data = session.query(Measurement.date, Measurement.prcp).all()
    for i in range(len(data)):
        key = data[i][0]
        if key not in pre_json.keys():
            pre_json[key] = [data[i][1]]
        else:
            pre_json[key] += [data[i][1]]
    return jsonify(pre_json)

@app.route("/api/v1.0/stations")
def stations():
    station_ls = []
    data = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    for station, name, lat, lon, elev in data:
        temp= {}
        temp["station"] = station
        temp["name"] = name
        temp["latitude"] = lat
        temp["longitude"] = lon
        temp["elevation"] = elev
        station_ls.append(temp)
    return jsonify(station_ls)

@app.route("/api/v1.0/tobs")
def temperature():
    pre_json = {}
    latest = session.query(Measurement).order_by(Measurement.date.desc()).first()
    latest = latest.__dict__["date"]
    year_ago= dt.datetime.strptime(latest, "%Y-%m-%d") + dt.timedelta(days=-365)
    year_ago= dt.date.isoformat(year_ago)
    whole_year = session.query(Measurement.date,Measurement.tobs).\
        filter(Measurement.date >= year_ago).all()
    for date, tobs in whole_year:
        if date not in pre_json.keys():
            pre_json[date] = [tobs]
        else:
            pre_json[date] += [tobs]
    return jsonify(pre_json)

@app.route("/api/v1.0/<start>")
def trip_begin(start):
    temp = {}
    data = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs) ,func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    minimum, average, maximum = data[0][0], data[0][1], data[0][2]
    temp["TMIN"] = minimum
    temp["TAVG"] = average
    temp["TMAX"] = maximum
    return jsonify(temp)

@app.route("/api/v1.0/<start>/<end>")
def trip(start,end):
    temp = {}
    data = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs) ,func.max(Measurement.tobs))\
        .filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    minimum, average, maximum = data[0][0], data[0][1], data[0][2]
    temp["TMIN"] = minimum
    temp["TAVG"] = average
    temp["TMAX"] = maximum
    return jsonify(temp)

if __name__ == "__main__":
    app.run(debug=True)