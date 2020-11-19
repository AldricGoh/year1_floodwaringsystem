from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    #Build list of stations
    stations = build_station_list()
    
    #Update water levels
    update_water_levels(stations)

    #Make a list of top N stations with highest water levels
    z = stations_highest_rel_level(stations, 10)

    #Print list, formatted
    for x in range(len(z)):
        print("Station and current level: " + str(z[x]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")    
    run()