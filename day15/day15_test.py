import pytest
from day15 import *

def test_example2():
    file_name = "example2"

    grid,instructions,robot_loc,nr_rows,nr_cols = parse_input(file_name)

    assert instructions == "<^^>>>vv<v>>v<<"
    assert grid[(0,0)] is None
    assert grid[(7,7)] is None
    assert grid[(6,6)] == "."
    assert grid[(2,2)] == "@"
    assert grid[(2,1)] is None
    assert grid[(1,3)] == "O"
    
    
    grid = follow_instructions(grid,instructions,robot_loc)
    coordinate_sum = determine_gps_coordinates(grid)

    assert coordinate_sum == 2028

def test_example1():
    file_name = "example1"

    grid,instructions,robot_loc,nr_rows,nr_cols = parse_input(file_name)

    assert instructions == "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
    assert grid[(4,4)] == "@"

    grid = follow_instructions(grid,instructions,robot_loc)
    coordinate_sum = determine_gps_coordinates(grid)

    assert coordinate_sum == 10092
    