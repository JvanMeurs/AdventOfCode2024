def next_secret_number(sec_nr):
    sec_nr ^= (sec_nr << 6) & 0xFFFFFF
    sec_nr ^= (sec_nr >> 5) & 0xFFFFFF
    sec_nr ^= (sec_nr << 11) & 0xFFFFFF
    return sec_nr

def run_sequence(memory,sec_nr,nr_runs,sequences,i,empty_seq):
    seq = []
    for _ in range(nr_runs):
        dig0 = sec_nr % 10
        if sec_nr not in memory:
            memory[sec_nr] = next_secret_number(sec_nr)
        sec_nr = memory[sec_nr]
        dig1 = sec_nr % 10
        seq.append(dig1-dig0)
        if len(seq) < 4:
            continue
        if len(seq) > 4:
            seq = seq[1:]
        key = str(seq)
        if key not in sequences:
            sequences[key] = empty_seq[:]
            sequences[key][i] = dig1
            continue
        if sequences[key][i] == 0:
            sequences[key][i] = dig1
    return sec_nr,sequences

def read_input(file_name):
    with open(file_name,'r') as file:
        return [int(line) for line in file]

def main():
    file_name = "input"
    nr_runs = 2000
    memory = {}
    sequences = {}
    calc_sec = []
    org_sec = read_input(file_name)

    empty_seq = [0 for _ in range(len(org_sec))]

    for i in range(len(org_sec)):
        sec_nr, sequences = run_sequence(memory,org_sec[i],nr_runs,sequences,i,empty_seq)
        calc_sec.append(sec_nr)

    best_value = 0
    for bananas in sequences.values():
        summed_bananas = sum(bananas)
        if summed_bananas > best_value:
            best_value = summed_bananas

    print(f"Answer day 22 part 1: {sum(calc_sec)}")    
    print(f"Answer day 22 part 2: {best_value}")

if __name__ == ("__main__"):
    main()