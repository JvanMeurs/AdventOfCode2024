import re
def parse_input(file_name):
    with open(file_name,'r') as input_data:
        lines = input_data.readlines()

    reg = {}
    for i,line in enumerate(lines):
        if i == 0:
            reg["A"] = int(re.findall(r"\d+",line)[0])
        if i == 1:
            reg["B"] = int(re.findall(r"\d+",line)[0])
        if i == 2:
            reg["C"] = int(re.findall(r"\d+",line)[0])
        if i == 4:
            program = list(map(int,re.findall(r"\d+",line)))
    return reg,program

def run_program(program,reg):
    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: reg["A"],
        5: reg["B"],
        6: reg["C"],
        7: None
    }

    output = []
    i = 0

    def run_instruction(instruction,operand,i):
        match instruction:
            case 0:
                reg["A"] = reg["A"] // (2**combo[operand])
                combo[4] = reg["A"]
            case 1:
                reg["B"] = reg["B"] ^ operand
                combo[5] = reg["B"]
            case 2:
                reg["B"] = (combo[operand] % 8) & 0b111
                combo[5] = reg["B"]
            case 3:
                if reg["A"] != 0:
                    return operand
            case 4:
                reg["B"] = reg["B"] ^ reg["C"]
                combo[5] = reg["B"]
            case 5:
                output.append(combo[operand] % 8)
            case 6:
                reg["B"] = reg["A"] // (2**combo[operand])
                combo[5] = reg["B"]
            case 7:
                reg["C"] = reg["A"] // (2**combo[operand])
                combo[6] = reg["C"]
        return i + 2

    while i < len(program):
        i = run_instruction(program[i],program[i+1],i)

    return ",".join(list(map(str, output)))

if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    reg, program = parse_input(file_name)
    print(f"Answer to day 17 part 1 is: {run_program(program,reg)}")