from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():

    #Build list of stations
    stations = build_station_list()
    
    #Update water levels
    update_water_levels(stations)

    #Make list of stations and relative wl with wl > some float
    z = stations_level_over_threshold(stations, 0.8)

    #Print list, formatted
    for x in range(len(z)):
        print("Station and current level: " + str(z[x]))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")    
    run()