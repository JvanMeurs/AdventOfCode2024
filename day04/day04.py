#strategy. Search rows, Search columns, Search Diagonals
import re
import numpy as np


def read_input(file_name):
    return [line.strip() for line in open(file_name).readlines()]

def get_all_strings(data):
    max_row = len(data)
    max_col = len(data[0])
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)] 
    fdiag = [[]for _ in range(max_col + max_row - 1)]
    bdiag = [[]for _ in range(max_col + max_row - 1)]

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(data[x][y])
            rows[y].append(data[x][y])
            fdiag[x+y].append(data[x][y])
            bdiag[x-y+max_row-1].append(data[x][y])

    return cols, rows, fdiag, bdiag

def join_strings(data):
    return ["".join(word) for word in data]

def count_matches(data):
    return sum(len(re.findall(r"XMAS",i) + re.findall(r"SAMX",i)) for i in data)

def find_match(data):
    return (re.match(r"MAS",data) or re.match(r"SAM",data))

def first_assignment(file_name):
    cols, rows, fdiag, bdiag = get_all_strings(read_input(file_name))
    return count_matches(join_strings(cols + rows + fdiag + bdiag))

def second_assignment(file_name):
    rows, _, _, _ = get_all_strings(read_input(file_name))

    sum = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            try:
                word1 = f"{rows[i][j]}{rows[i+1][j+1]}{rows[i+2][j+2]}"
                word2 = f"{rows[i+2][j]}{rows[i+1][j+1]}{rows[i][j+2]}"
                if find_match(word1) and find_match(word2):
                    sum += 1
            except:
                continue        
    
    return sum
    
if __name__ == ("__main__"):
    print(first_assignment("sample_input.txt"))
    print(first_assignment("input.txt"))
    
    print(second_assignment("sample_input.txt"))
    print(second_assignment("input.txt"))


