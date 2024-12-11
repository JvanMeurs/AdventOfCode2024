import pytest
from day11 import *

def test_input_reading():
    file_name = "sample_input"
    data = read_input(file_name)
    assert len(data) == 5
    assert data == ['0', '1', '10', '99', '999']

def test_single_blink():
    file_name = "sample_input"
    stones = read_input(file_name)
    assert stones == ['0', '1', '10', '99', '999']
    stones = blink(stones)
    assert len(stones) == 7
    assert stones == ['1', '2024', '1', '0', '9', '9', '2021976']
    
def test_multi_blink():
    stones = ['125', '17']

    stones = blink(stones)
    assert stones == ['253000', '1', '7']
    
    stones = blink(stones)
    assert stones == ['253', '0', '2024', '14168']

    stones = blink(stones)
    assert stones == ['512072', '1', '20', '24', '28676032']

    stones = blink(stones)
    assert stones == ['512', '72', '2024', '2', '0', '2', '4', '2867', '6032']
    
    stones = blink(stones)
    assert stones == ['1036288', '7', '2', '20', '24', '4048', '1', '4048', '8096', '28', '67', '60', '32']

    stones = blink(stones)
    assert len(stones) == 22
    assert stones == ['2097446912', '14168', '4048', '2', '0', '2', '4', '40', '48', '2024', '40', '48', '80', '96', '2', '8', '6', '7', '6', '0', '3', '2']
    
    for _ in range(25-6):
        stones = blink(stones)

    assert len(stones) == 55312

def test_count_stones_25():
    stones = ['125', '17']
    nr_blinks = 25
    assert count_stones(stones,nr_blinks) == 55312


def test_count_stones_25_dict():
    stones = ['125', '17']
    nr_blinks = 25
    stones = parse_input(stones)
    assert count_stones_dict(stones,nr_blinks) == 55312