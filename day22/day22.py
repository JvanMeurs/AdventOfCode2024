def mix(sec_nr,nr):
    return sec_nr ^ nr

def prune(sec_nr):
    return sec_nr & 0xFFFFFF

def next_secret_number(sec_nr):
    sec_nr ^= (sec_nr << 6) & 0xFFFFFF
    sec_nr ^= (sec_nr >> 5) & 0xFFFFFF
    sec_nr ^= (sec_nr << 11) & 0xFFFFFF
    return sec_nr

def run_sequence(memory,sec_nr,nr_runs):
    for _ in range(nr_runs):
        if sec_nr not in memory:
            memory[sec_nr] = next_secret_number(sec_nr)
        sec_nr = memory[sec_nr]
    return sec_nr

def read_input(file_name):
    with open(file_name,'r') as file:
        return [int(line) for line in file]

def main():
    file_name = "input"
    nr_runs = 2000
    memory = {}
    calc_sec = []
    org_sec = read_input(file_name)

    for i in range(len(org_sec)):
        sec_nr = run_sequence(memory,org_sec[i],nr_runs)
        calc_sec.append(sec_nr)

    print(f"Answer day 22 part 1: {sum(calc_sec)}")

if __name__ == ("__main__"):
    main()