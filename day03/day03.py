import re

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def find_mul(data):
    return re.findall(r"mul\(\d+,\d+\)",data)

def find_digit(data):
    return re.findall(r"\d+",data)


def multiply_and_sum(data):
    return sum(int(i) * int(j) for [i,j] in (find_digit(mul) for mul in find_mul(data)))

if __name__ == ("__main__"):
    with open("sample_input.txt",'r') as input_file:
        data = input_file.read()

    print(multiply_and_sum(data))

    with open("input.txt",'r') as input_file:
        data = input_file.read()

    print(multiply_and_sum(data))
