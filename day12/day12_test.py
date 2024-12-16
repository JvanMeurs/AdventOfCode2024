import pytest
from day12 import *

def test_example1():
    file_name = "example1"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs,bulk_costs = calculate_total_cost(plants)
    assert plants[0]["area"] == 4
    assert plants[0]["perimeter"] == 10
    assert plants[0]["sides"] == 4
    assert plants[1]["area"] == 4
    assert plants[1]["perimeter"] == 8
    assert plants[1]["sides"] == 4
    assert plants[2]["area"] == 4
    assert plants[2]["perimeter"] == 10
    assert plants[2]["sides"] == 8
    assert plants[3]["area"] == 1
    assert plants[3]["perimeter"] == 4
    assert plants[3]["sides"] == 4
    assert plants[4]["area"] == 3
    assert plants[4]["perimeter"] == 8
    assert plants[4]["sides"] == 4
    assert len(plants) == 5
    assert costs == 140
    assert bulk_costs == 80

def test_example2():
    file_name = "example2"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs,bulk_costs = calculate_total_cost(plants)
    assert plants[0]["area"] == 21
    assert plants[0]["perimeter"] == 36
    assert plants[1]["area"] == 1
    assert plants[1]["perimeter"] == 4
    assert plants[2]["area"] == 1
    assert plants[2]["perimeter"] == 4
    assert plants[3]["area"] == 1
    assert plants[3]["perimeter"] == 4
    assert plants[4]["area"] == 1
    assert plants[4]["perimeter"] == 4
    assert len(plants) == 5
    assert costs == 772
    assert bulk_costs == 436

def test_example3():
    file_name = "example3"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs, bulk_costs = calculate_total_cost(plants)
    assert plants[0]["area"] == 12
    assert plants[0]["perimeter"] == 18
    assert plants[0]["sides"] == 10
    assert plants[1]["area"] == 4
    assert plants[1]["perimeter"] == 8
    assert plants[1]["sides"] == 4
    assert plants[2]["area"] == 14
    assert plants[2]["perimeter"] == 28
    assert plants[2]["sides"] == 22
    assert plants[3]["area"] == 10
    assert plants[3]["perimeter"] == 18
    assert plants[3]["sides"] == 12
    assert plants[4]["area"] == 13
    assert plants[4]["perimeter"] == 20
    assert plants[4]["sides"] == 10
    assert plants[5]["area"] == 11
    assert plants[5]["perimeter"] == 20
    assert plants[5]["sides"] == 12
    assert plants[6]["area"] == 1
    assert plants[6]["perimeter"] == 4
    assert plants[6]["sides"] == 4
    assert plants[7]["area"] == 13
    assert plants[7]["perimeter"] == 18
    assert plants[7]["sides"] == 8
    assert plants[8]["area"] == 14
    assert plants[8]["perimeter"] == 22
    assert plants[8]["sides"] == 16
    assert plants[9]["area"] == 5
    assert plants[9]["perimeter"] == 12
    assert plants[9]["sides"] == 6
    assert plants[10]["area"] == 3
    assert plants[10]["perimeter"] == 8
    assert plants[10]["sides"] == 6
    assert len(plants) == 11
    assert costs == 1930
    assert bulk_costs == 1206

def test_example4():
    file_name = "example4"
    data = read_input(file_name)
    plants = traverse_grid(data)
    _, bulk_costs = calculate_total_cost(plants)
    assert len(plants) == 3
    assert plants[0]["area"] == 17
    assert plants[0]["sides"] == 12
    assert plants[1]["area"] == 4
    assert plants[1]["sides"] == 4
    assert plants[2]["area"] == 4
    assert plants[2]["sides"] == 4
    assert bulk_costs == 236

def test_example5():
    file_name = "example5"
    data = read_input(file_name)
    plants = traverse_grid(data)
    _, bulk_costs = calculate_total_cost(plants)
    assert len(plants) == 3
    assert plants[0]["area"] == 28
    assert plants[0]["sides"] == 12
    assert plants[1]["area"] == 4
    assert plants[1]["sides"] == 4
    assert plants[2]["area"] == 4
    assert plants[2]["sides"] == 4
    assert bulk_costs == 368