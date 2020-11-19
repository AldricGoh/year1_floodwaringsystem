from floodsystem.geo import stations_within_radius
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list

def run():
    
    coordinate = (52.2053, 0.1218)

    stations = build_station_list()
    
    print(stations_within_radius(stations, coordinate, 10))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")    
    run()