import math

def sum_all(total,elements):
    return total == sum(elements)

def multiply_all(total, elements):
    return total == math.prod(elements)

def read_input(file_name):
    with open(file_name,'r') as input:
        return input.read().strip().splitlines()

def get_total_sum(data,list_func):
    sum_pass = 0
    for line in data:
        total = int(line.split(":")[0])
        elements = [int(i) for i in line.split(":")[1].split()]

        elements_list = [elements[0]]
        for idx in range(len(elements)-1):
            temp = []
            for val in elements_list:
                if val > total:
                    continue
                temp += list_func(val,elements[idx+1])
            elements_list = temp
   
        if total in elements_list:
            sum_pass += total
        
    return sum_pass

def add_multiply(val,element):
    return [val + element, val * element]


def add_multiply_concat(val,element):
    return [val + element, val * element, int(f"{val}{element}")]

if __name__ == ("__main__"):
    file_name = "sample_input.txt"
    data = read_input(file_name)
    total_sum = get_total_sum(data,add_multiply)
    print(f"Sample answer part 1: {total_sum}")

    total_sum = get_total_sum(data,add_multiply_concat)
    print(f"Sample answer part 2: {total_sum}")

    file_name = "input"
    data = read_input(file_name)
    total_sum = get_total_sum(data,add_multiply)
    print(f"Answer part 1: {total_sum}")

    total_sum = get_total_sum(data,add_multiply_concat)
    print(f"Answer part 2: {total_sum}")
