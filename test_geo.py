"""Unit test for the geographical module

"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import *
from floodsystem.geo import *
from floodsystem.flood import *

def fake_station_list(n):
    """ Build a list of station to test program built """
    
    alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
    num = [i for i in range(0, 200)]

    station = []
    print(n)
    for x in range(n -1):
        # Create a station
        s_id = alpha[x]
        m_id = alpha[x]
        label = alpha[x]
        coord = (num[x], num[x+1])
        trange = (num[x+2], num[x+3])
        river = alpha[x]
        town = alpha[x]
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
        s.latest_level = num[x+3]
        station.append(s)

    s_id = "Extra"
    m_id = "Extra"
    label = "a"
    coord = (0, 1)
    trange = (2, 3)
    river = "a"
    town = "a"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 100
    station.append(s)    

    return station

def test_stations_distance():
    """ Test for list of stations based on distance """
    #Build list of station
    station_list = fake_station_list(5)
    
    #Set parameter P with results we know of
    p = (0,0)

    #Run function
    x = stations_by_distance(station_list, p)
    for i in range(len(x)-1):
        if x[i][2] > x[i+1][2]:
            raise ValueError("Sorting distance should be from closest to furthest!")
    
    assert type(x) == list

def test_stations_within_radius():
    """ Test for list of stations within a certain radius """
    coordinate = (0, 0)

    stations = fake_station_list(20)

    y = stations_within_radius(stations, coordinate, 401)
    
    assert type(y) == list

    if len(y) != 4:
        raise ValueError("Function Error")

def test_rivers():
    """ Test if rivers which has stations at compiled into a set """
    #Build list of station
    station_list = fake_station_list(23)

    rivers = rivers_with_station(station_list)
    
    assert type(rivers) == list
    assert len(rivers) == 22
    assert 'c' in rivers
    assert 'g' in rivers

def test_stations_at_rivers():
    """ Test if stations at river are paired with the river in a dictionary """
    #Build list of station
    station_list = fake_station_list(5)

    dic = stations_by_river(station_list)

    assert type(dic) == dict
    assert len(dic) == 4

def test_station_count():
    """Test if function rivers_by_station_number works correctly"""
    #Build list of station
    station_list = fake_station_list(5)

    a = rivers_by_station_number(station_list, 1)

    assert type(a) == list
    assert len(a) == 1

def test_stations_over_threshold():
    """Tests if function stations_level_over_threshold works correctly"""
    #Build list of stations
    station_list = fake_station_list(5)

    a = stations_level_over_threshold(station_list, 1.1)

    assert type(a) == list
    assert len(a) == 1

def test_highest_rel_level():
    """Tests if function stations_highest_rel_level works correctly"""
    #Build list of stations
    station_list = fake_station_list(5)

    a = stations_highest_rel_level(station_list, 2)

    for i in range(len(a)-1):
        if a[i][1] < a[i+1][1]:
            raise ValueError("Relative water level should be ordered from highest to lowest")

    assert type(a) == list
    assert len(a) == 2
    