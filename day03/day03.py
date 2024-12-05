import re

def find_mul(data):
    return re.findall(r"mul\(\d+,\d+\)",data)

def find_digit(data):
    return re.findall(r"\d+",data)

def filter_dont(data):
    return (re.split(r"don't\(\)",j)[0] for j in re.split(r"do\(\)",data))

def multiply_and_sum(data):
    return sum(int(i) * int(j) for [i,j] in (find_digit(mul) for mul in find_mul(data)))

def filter_intructions(data):
    return sum(multiply_and_sum(i) for i in filter_dont(data))

if __name__ == ("__main__"):
    with open("sample_input.txt",'r') as input_file:
        data = input_file.read()

    print(multiply_and_sum(data))
    print(filter_intructions(data))

    with open("input.txt",'r') as input_file:
        data = input_file.read()

    print(multiply_and_sum(data))
    print(filter_intructions(data))
