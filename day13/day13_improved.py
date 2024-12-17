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


def solve_single_input(data):
    b = (data["Ax"]*data["y"] - data["Ay"]*data["x"]) // (data["Ax"]*data["By"] - data["Ay"]*data["Bx"])
    a = (data["x"]*data["By"] - data["y"]*data["Bx"]) // (data["Ax"]*data["By"] - data["Ay"]*data["Bx"])
    if data["Ax"]*a+data["Bx"]*b==data["x"] and data["Ay"]*a+data["By"]*b==data["y"]:
        return 3*a+b
    else:
        return 0

def get_minimal_tokens(data,offset):
    tokens = 0
    for entry in data:
        entry["x"] += offset
        entry["y"] += offset
        tokens += solve_single_input(entry)
    return tokens

if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    offset = 0                
    data = parse_input(file_name)
    print(f"Answer day 13 part 1: {get_minimal_tokens(data,offset)}")

    offset = 10000000000000
    data = parse_input(file_name)
    print(f"Answer day 13 part 2: {get_minimal_tokens(data,offset)}")

