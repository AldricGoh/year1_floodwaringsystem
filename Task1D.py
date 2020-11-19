from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    rivers = rivers_with_station(stations)
    river_stations = stations_by_river(stations)

    # Print number of rivers
    print("Number of rivers with at least 1 station: {}".format(len(rivers)))

    #Print first 10 rivers in alphabetical order
    print("-- First 10 rivers in alphabetical order: --")
    print(rivers[:10])

    #Print stations by river
    #River Aire
    print("-- Stations by River Aire: --")
    print(river_stations["River Aire"])

    #River Cam
    print("-- Stations by River Cam: --")
    print(river_stations["River Cam"])

    #River Thames
    print("-- Stations by River Thames: --")
    print(river_stations["River Thames"])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()