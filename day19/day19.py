
def parse_input(file_name):
    with open(file_name,'r') as file_content:
        lines = file_content.read().strip().split("\n")
    substrings = set([s.strip() for s in lines[0].split(",")])
    targets = [line.strip() for line in lines[2:]]

    return substrings, targets

def count_ways_to_form_target(target, substrings, available_chars,max_len):

    if not set(target).issubset(available_chars):
        return 0

    dp = [0] * (len(target) + 1)
    dp[0] = 1
    
    for i in range(1, len(target) + 1):
        for length in range(1, max_len + 1):
            if i >= length and target[i - length:i] in substrings:
                dp[i] += dp[i - length]
    
    return dp[len(target)]

def count_all_ways(targets, substrings):
    nr_proper_targets = 0
    all_ways = 0

    available_chars = set("".join(substrings))
    max_len = max(len(sub) for sub in substrings)
    
    for target in targets:
        nr_ways =  count_ways_to_form_target(target, substrings, available_chars, max_len)
        nr_proper_targets += (nr_ways != 0)
        all_ways += nr_ways

    return nr_proper_targets,all_ways

if __name__ == ("__main__"):
    input_file = "example1"
    substrings, targets = parse_input(input_file)
    nr_proper_targets, all_ways = count_all_ways(targets,substrings)
    print(f"Example 1 number of possible designs: {nr_proper_targets}")
    print(f"Example 2 number of distinct ways to create all designs: {all_ways}")
    
    input_file = "input"
    substrings, targets = parse_input(input_file)
    nr_proper_targets, all_ways = count_all_ways(targets,substrings)
    print(f"Answer day 19 part 1: {nr_proper_targets}")
    print(f"Answer day 19 part 2: {all_ways}")
    