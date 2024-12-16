import pytest
from day12 import *

def test_example1():
    file_name = "example1"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs = calculate_total_cost(plants)
    assert plants[0]["area"] == 4
    assert plants[0]["perimiter"] == 10
    assert plants[1]["area"] == 4
    assert plants[1]["perimiter"] == 8
    assert plants[2]["area"] == 4
    assert plants[2]["perimiter"] == 10
    assert plants[3]["area"] == 1
    assert plants[3]["perimiter"] == 4
    assert plants[4]["area"] == 3
    assert plants[4]["perimiter"] == 8
    assert len(plants) == 5
    assert costs == 140

def test_example2():
    file_name = "example2"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs = calculate_total_cost(plants)
    assert plants[0]["area"] == 21
    assert plants[0]["perimiter"] == 36
    assert plants[1]["area"] == 1
    assert plants[1]["perimiter"] == 4
    assert plants[2]["area"] == 1
    assert plants[2]["perimiter"] == 4
    assert plants[3]["area"] == 1
    assert plants[3]["perimiter"] == 4
    assert plants[4]["area"] == 1
    assert plants[4]["perimiter"] == 4
    assert len(plants) == 5
    assert costs == 772

def test_example3():
    file_name = "example3"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs = calculate_total_cost(plants)
    assert plants[0]["area"] == 12
    assert plants[0]["perimiter"] == 18
    assert plants[1]["area"] == 4
    assert plants[1]["perimiter"] == 8
    assert plants[2]["area"] == 14
    assert plants[2]["perimiter"] == 28
    assert plants[3]["area"] == 10
    assert plants[3]["perimiter"] == 18
    assert plants[4]["area"] == 13
    assert plants[4]["perimiter"] == 20
    assert plants[5]["area"] == 11
    assert plants[5]["perimiter"] == 20
    assert plants[6]["area"] == 1
    assert plants[6]["perimiter"] == 4
    assert plants[7]["area"] == 13
    assert plants[7]["perimiter"] == 18
    assert plants[8]["area"] == 14
    assert plants[8]["perimiter"] == 22
    assert plants[9]["area"] == 5
    assert plants[9]["perimiter"] == 12
    assert plants[10]["area"] == 3
    assert plants[10]["perimiter"] == 8
    assert len(plants) == 11
    assert costs == 1930