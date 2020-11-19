# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_consistency():

    # Create stations with incorrect & correct data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label_1 = "Upper < lower limit"
    label_2 = "No range"
    label_3 = "Correct!"
    coord = (-2.0, 4.0)
    trange_1 = (5, 4)
    trange_2 = None
    trange_3 = (2, 3)
    river = "River X"
    town = "My Town"
    s_false1 = MonitoringStation(s_id, m_id, label_1, coord, trange_1, river, town)
    s_false2 = MonitoringStation(s_id, m_id, label_2, coord, trange_2, river, town)
    s_true = MonitoringStation(s_id, m_id, label_3, coord, trange_3, river, town)

    assert MonitoringStation.typical_range_consistent(s_false1) == False
    assert MonitoringStation.typical_range_consistent(s_false2) == False
    assert MonitoringStation.typical_range_consistent(s_true) == True
    
    z = [s_false1, s_false2, s_true]
    assert type(inconsistent_typical_range_stations(z)) == list
    assert len(inconsistent_typical_range_stations(z)) == 2
    assert inconsistent_typical_range_stations(z) == ["No range", "Upper < lower limit"]