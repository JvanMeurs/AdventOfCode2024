from ortools.sat.python import cp_model
import re

def parse_input(file_name):
    with open(file_name,'r') as input_file:
        lines = input_file.readlines()

    data = []
    for i in range(0,len(lines),4):
        inner_data = {}
        for j in range(3):
            x_num = re.findall(r'\d+',re.findall(r'X[+=]\d+', lines[i+j])[0])
            y_num = re.findall(r'\d+',re.findall(r'Y[+=]\d+', lines[i+j])[0])
            if j == 0:
                x_key = "Ax"
                y_key = "Ay"
            if j == 1:
                x_key = "Bx"
                y_key = "By"
            if j == 2:
                x_key = "x"
                y_key = "y"
                
            inner_data[x_key] = int(x_num[0])
            inner_data[y_key] = int(y_num[0])

        data.append(inner_data)
    return data

def setup_model():
    model = cp_model.CpModel()
    return model

def solve_single_input(model,data,maximum,addition):

    A = model.new_int_var(0, maximum, 'A')
    B = model.new_int_var(0, maximum, 'B')

    model.Minimize(3*A+B)

    model.Add(A*data["Ax"] + B*data["Bx"] == data["x"] + addition) # Food
    model.Add(A*data["Ay"] + B*data["By"] == data["y"] + addition) # Food

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL:
        minimum_tokens = solver.ObjectiveValue()
        return minimum_tokens
    else:
         return None

def get_minimal_tokens(data,model,maximum=100,addition=0):
    minimal_tokens = 0
    for i in data:
        solution = solve_single_input(model.clone(),i,maximum,addition)
        if solution is not None:
            minimal_tokens += solution
    return minimal_tokens

if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    data = parse_input(file_name)
    model = setup_model()
    print(f"Answer day 13 part 1: {get_minimal_tokens(data,model)}")
    print(f"Answer day 13 part 2: {get_minimal_tokens(data,model,2**18,10000000000000)}")