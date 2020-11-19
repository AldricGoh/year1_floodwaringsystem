from floodsystem.stationdata import build_station_list
from floodsystem.geo import * 
from floodsystem.plot import *
from floodsystem.flood import *
from floodsystem.datafetcher import fetch_measure_levels
from datetime import *

def run():
    """Requirements for Task 2E"""

    #Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 5)

    station_true = []
    for i in range(len(station)):
        station_true.append([stations[x] for x in range(len(stations)) if  stations[x].name == station[i][0]])
    
    for i in range(len(station_true)):
        dt = 10
        dates, levels = fetch_measure_levels(station_true[i][0].measure_id, dt=timedelta(days=dt))
        plot_water_levels(station_true[i][0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()