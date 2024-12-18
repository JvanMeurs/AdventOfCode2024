import pytest
from day14 import *

def test_parse():
    file_name = "example1"
    data = parse_input(file_name)

    assert len(data) == 12
    assert data[0]["pos"] == (0,4)
    assert data[0]["vel"] == (3,-3)

def test_single_example():
    data = {"pos":(2,4),"vel":(2,-3)}
    max_x = 11
    max_y = 7
    next_pos_dict = {}
    
    next_pos_dict, data = update_pos(next_pos_dict,data,max_x,max_y)
    assert data["pos"] == (4,1)

    next_pos_dict, data = update_pos(next_pos_dict,data,max_x,max_y)
    assert data["pos"] == (6,5)

    next_pos_dict, data = update_pos(next_pos_dict,data,max_x,max_y)
    assert data["pos"] == (8,2)

    next_pos_dict, data = update_pos(next_pos_dict,data,max_x,max_y)
    assert data["pos"] == (10,6)
    
    next_pos_dict, data = update_pos(next_pos_dict,data,max_x,max_y)
    assert data["pos"] == (1,3)

def test_example1():
    file_name = "example1"
    data = parse_input(file_name)
    max_x = 11
    max_y = 7
    nr_secs=100
    next_pos_dict = {}

    data,_,_ = loop_data(next_pos_dict, data, nr_secs, max_x, max_y)
    q1_robots,q2_robots,q3_robots,q4_robots = get_safety_score_per_quadrant(data,max_x,max_y)
    safety_score = get_safety_score(q1_robots,q2_robots,q3_robots,q4_robots)

    assert q1_robots == 1
    assert q2_robots == 3
    assert q3_robots == 4
    assert q4_robots == 1
    assert safety_score == 12