#import dependencies
import numpy as np
import pandas as pd
import datetime as dt
from flask import Flask, jsonify

#Connect to Database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model (ORM takes table sand converts to python classes)

Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement= Base.classes.measurement
Station= Base.classes.station

#create variable that holds server
app = Flask(__name__)
#Provide flask with "route/predetermined request"/ endpoint 

#Creation of index/homepage
@app.route("/")
def homepage():
    return (
        "<h1>API Routes</h1>"
        "/api/v1.0/precipitation<br>"
        "/api/v1.0/stations<br>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #create session link from python to the Database
    session = Session(engine)
    last12months = dt.date(2017,8,23)-dt.timedelta(days=365)
    dandp = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>= last12months).all()
    return_data = {}

    for row in dandp:
        pdate=row[0]
        prcp = row[1]
        return_data[pdate] = prcp

    session.close()
    return jsonify(return_data)
        

@app.route("/api/v1.0/stations")
def stations():
    #create session link from python to the Database
    session = Session(engine)
    listofstations = session.query(Measurement.station).distinct().all()

    session.close()

    all_stations=list(np.ravel(listofstations))
    return jsonify(all_stations)



@app.route("/api/v1.0/tobs")
def tobs():
    #create session link from python to the Database
    session = Session(engine)
    last12months = dt.date(2017,8,23)-dt.timedelta(days=365)
    stationdata = session.query(Measurement.date, Measurement.tobs).filter((Measurement.date>= last12months) & (Measurement.station=="USC00519281")).all()
  
    session.close()

    all_tobs=list(np.ravel(stationdata))
    return jsonify(all_tobs)



@app.route("/api/v1.0/<start_day>")
def start_date(start_day):
    #create session link from python to the Database
    session = Session(engine)
    stationdata = session.query(func.min(Measurement.tobs),
              func.max(Measurement.tobs),
              func.avg(Measurement.tobs)
              ).filter(Measurement.date >= start_day).first()
    session.close()
    print(stationdata)
    return {"min":stationdata[0], "max": stationdata[1], "average": stationdata[2]}


@app.route("/api/v1.0/<start_day>/<end_day>")
def end_date(start_day,end_day):
    #create session link from python to the Database
    session = Session(engine)
    print(start_day, end_day)
    stationdata = session.query(func.min(Measurement.tobs),
              func.max(Measurement.tobs),
              func.avg(Measurement.tobs)
              ).filter(Measurement.date >= start_day).filter(Measurement.date <= end_day).first()
    print(stationdata)
    session.close()
    return {"min":stationdata[0], "max": stationdata[1], "average": stationdata[2]}
    

if __name__ =="__main__":
    app.run(debug=True)

