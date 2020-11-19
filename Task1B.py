from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    #Set p to coordinates of cambridge centre:
    p = (52.2053, 0.1218)

    # List of distances of stations:
    L = stations_by_distance(stations, p)

    print("Closest 10 stations:")
    print(L[:10])
    print("Furthest 10 stations:")
    print(L[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()