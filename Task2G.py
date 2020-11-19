from floodsystem.stationdata import build_station_list
from floodsystem.station import *
from floodsystem.geo import * 
from floodsystem.plot import *
from floodsystem.flood import *
from floodsystem.datafetcher import fetch_measure_levels
from datetime import *
from floodsystem.analysis import *
import numpy as np

def run():
    """Requirements for Task 2G"""

    #Build list of stations
    stations = build_station_list()
    
    #Determine which stations can be computed
    valid_stations = [stations[x] for x in range(len(stations)) if MonitoringStation.typical_range_consistent(stations[x]) == True]
    #Update water levels
    update_water_levels(valid_stations)
    
    invalid = []
    for x in range(len(valid_stations)):
        if MonitoringStation.relative_water_level(valid_stations[x]) is None:
            invalid.append(valid_stations[x])
        else:
            pass
    
    valid_stations = [x for x in valid_stations if x not in invalid]

    print(len(valid_stations))


    #Only worried about station if water level is above average
    stations_level = stations_level_over_threshold(stations, 0.5)
    station_over_tol = []
    for i in range(len(stations_level)):
        for x in range(len(valid_stations)):
            if valid_stations[x].name == stations_level[i][0] and MonitoringStation.relative_water_level(valid_stations[x]) == stations_level[i][1]:
                station_over_tol.append(valid_stations[x]) 
            else:
                pass
    
    #Determine rivers at risk
    stations_to_river = stations_by_river(station_over_tol)

    #Set up lists for categorising risks at rivers
    rivers_low = []
    rivers_moderate =[]
    rivers_high = []
    rivers_severe = []

    #Fetch water levels from pass 2 days & compare
    dt = 2

    #Evaluate average relative water levels at rivers & compare
    keys = list(stations_to_river.keys())
    values = list(stations_to_river.values())
    values_1 = []
    for i in range(len(values)):
        for x in range(len(values[i])):
            lst = [MonitoringStation.relative_water_level(station_over_tol[n]) for n in range(len(station_over_tol)) 
                if station_over_tol[n].name == values[i][x] and station_over_tol[n].river == keys[i]]
            values_1.append(sum(lst) / len(lst))
    
    for i in range(len(keys)):
        if values_1[i] < 0.8:
            rivers_low.append(keys[i])
        
        elif values_1[i] >= 0.8 and values_1[i] < 1:
            for n in range(len(station_over_tol)):
                if station_over_tol[n].river == keys[i]:
                    station = station_over_tol[n]
            dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
            if len(dates) == 0:
                m = 0
            else:
                poly, d0, m = polyfit(dates, levels, 4)
                gradient = np.polyder(poly)
                m = gradient(m) 
            if m <= 0:
                rivers_moderate.append(keys[i])
            else:
                rivers_high.append(keys[i])
        
        elif values_1[i] >= 1 and values_1[i] < 2:
            for n in range(len(station_over_tol)):
                if station_over_tol[n].river == keys[i]:
                    station = station_over_tol[n]
            dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
            if len(dates) == 0:
                m = 0
            else:
                poly, d0, m = polyfit(dates, levels, 4)
                gradient = np.polyder(poly)
                m = gradient(m) 
            if m <= 0:
                rivers_high.append(keys[i])
            else:
                rivers_severe.append(keys[i])
        else:
            rivers_severe.append(keys[i])
    
    towns_low = []
    towns_moderate = []
    towns_high = []
    towns_severe = []

    for i in range(len(rivers_low)):
        towns_low.append([station_over_tol[n].town for n in range(len(station_over_tol)) 
                if station_over_tol[n].river == rivers_low[i]])
    for i in range(len(rivers_moderate)):
        towns_moderate.append([station_over_tol[n].town for n in range(len(station_over_tol)) 
                if station_over_tol[n].river == rivers_moderate[i]])
    for i in range(len(rivers_high)):
        towns_high.append([station_over_tol[n].town for n in range(len(station_over_tol)) 
                if station_over_tol[n].river == rivers_high[i]])
    for i in range(len(rivers_severe)):
        towns_severe.append([station_over_tol[n].town for n in range(len(station_over_tol)) 
                if station_over_tol[n].river == rivers_severe[i]])

    print("--- Towns with low risks ---")
    print(towns_low)
    print("--- Towns with moderate risks ---")
    print(towns_moderate)
    print("--- Towns with high risks ---")
    print(towns_high)
    print("--- Towns with severe risks ---")
    print(towns_severe)

    #stations_highest_rel_level(stations, N)
    #print(type(station_over_tol[0].town))
    # stations_to_town = stations_by_town(station_over_tol)
    # print(len(stations_to_town)) 

    # values_1.append([station_over_tol[n] for n in range(len(station_over_tol)) 
    #             if station_over_tol[n].name == values[i][x] and station_over_tol[n].river == keys[i]])

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()