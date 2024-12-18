import pytest
from day17 import *

def test_1():
    reg = {
    "A": 0,
    "B": 0,
    "C": 9
    }

    run_program([2,6],reg)
    assert reg["B"] == 1

def test_2():
    reg = {
    "A": 10,
    "B": 0,
    "C": 0
    }

    assert run_program([5,0,5,1,5,4],reg) == "0,1,2"

def test_3():
    reg = {
    "A": 2024,
    "B": 0,
    "C": 0
    }

    assert run_program([0,1,5,4,3,0],reg) == "4,2,5,6,7,7,7,7,3,1,0"
    assert reg["A"] == 0

def test_4():
    reg = {
    "A": 0,
    "B": 29,
    "C": 0
    }
    run_program([1,7],reg)
    assert reg["B"] == 26    

def test_5():
    reg = {
    "A": 0,
    "B": 2024,
    "C": 43690
    }
    run_program([4,0],reg)
    assert reg["B"] == 44354

def test_example1():
    file_name = "example1"
    reg, program = parse_input(file_name)

    assert reg["A"] == 729
    assert reg["B"] == 0
    assert reg["C"] == 0
    assert program == [0,1,5,4,3,0]

    assert run_program(program,reg) == "4,6,3,5,6,3,5,2,1,0"