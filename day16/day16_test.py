import pytest
from day16 import *
    
def test_example1():
    file_name = "example1"
    grid,start,destination,nr_rows,nr_cols = parse_input(file_name)
    shortest_path_cost,visited,end = find_shortest_path(grid, start, destination)
    path_count = nr_unique_points_on_shortest_routes(visited,end)

    assert shortest_path_cost == 7036
    assert path_count == 45

def test_example2():
    file_name = "example2"
    grid,start,destination,nr_rows,nr_cols = parse_input(file_name)
    shortest_path_cost,visited,end = find_shortest_path(grid, start, destination)
    path_count = nr_unique_points_on_shortest_routes(visited,end)

    assert shortest_path_cost == 11048
    assert path_count == 64