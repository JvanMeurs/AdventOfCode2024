import pytest
from my_code import *

def test_input_processing():
    reports = read_input("sample_input.txt")
    assert len(reports) == 6
    assert reports[0] == [7,6,4,2,1]
    assert reports[1] == [1,2,7,8,9]
    assert reports[2] == [9,7,6,2,1]
    assert reports[3] == [1,3,2,4,5]
    assert reports[4] == [8,6,4,4,1]
    assert reports[5] == [1,3,6,7,9]

def test_strict_safety():
    reports = read_input("sample_input.txt")
    assert determine_safety_strict(reports[0]) == 1
    assert determine_safety_strict(reports[1]) == 0
    assert determine_safety_strict(reports[2]) == 0
    assert determine_safety_strict(reports[3]) == 0
    assert determine_safety_strict(reports[4]) == 0
    assert determine_safety_strict(reports[5]) == 1    

def test_lean_safety():
    reports = read_input("sample_input.txt")
    assert determine_safety_lean(reports[0]) == 1
    assert determine_safety_lean(reports[1]) == 0
    assert determine_safety_lean(reports[2]) == 0
    assert determine_safety_lean(reports[3]) == 1
    assert determine_safety_lean(reports[4]) == 1
    assert determine_safety_lean(reports[5]) == 1