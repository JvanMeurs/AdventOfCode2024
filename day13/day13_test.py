import pytest
from day13 import *

def test_input_parsing():
    file_name = "example1"
    data = parse_input(file_name)
    assert len(data) == 4

    assert data[0]["Ax"] == 94
    assert data[0]["Ay"] == 34
    assert data[0]["Bx"] == 22
    assert data[0]["By"] == 67
    assert data[0]["x"] == 8400
    assert data[0]["y"] == 5400

    assert data[3]["Ax"] == 69
    assert data[3]["Ay"] == 23
    assert data[3]["Bx"] == 27
    assert data[3]["By"] == 71
    assert data[3]["x"] == 18641
    assert data[3]["y"] == 10279

def test_first_input():
    file_name = "example1"
    data = parse_input(file_name)
    model = setup_model()

    solution = solve_single_input(model,data[0],100,0)

    assert solution is not None
    assert solution == 280


def test_all_inputs():
    file_name = "example1"
    data = parse_input(file_name)
    model = setup_model()

    solutions = []
    minimal_tokens = 0
    for i in data:
        solution = solve_single_input(model.clone(),i,100,0)
        solutions.append(solution)
        if solution is not None:
            minimal_tokens += solution
        
    assert solutions[0] is not None
    assert solutions[0] == 280
    assert solutions[1] is None
    assert solutions[2] is not None
    assert solutions[2] == 200
    assert solutions[3] is None
    assert minimal_tokens == 480

def test_minimal_tokens():
    file_name = "example1"
    data = parse_input(file_name)
    model = setup_model()
    assert get_minimal_tokens(data,model) == 480