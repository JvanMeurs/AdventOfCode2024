def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip().split('\n')[0].split()

def blink(stones_before_blink):
    stones_after_blink = []
    for stone in stones_before_blink:
        if stone == '0':
            stones_after_blink.append('1')
            continue
        stone_size = len(stone)
        if stone_size%2 == 0:
            stones_after_blink.append(stone[:stone_size//2])
            stones_after_blink.append(str(int(stone[stone_size//2:])))
            continue
        stones_after_blink.append(str(int(stone)*2024))
    return stones_after_blink

def count_stones(stones,nr_blinks):
    for _ in range(nr_blinks):
        stones = blink(stones)
    return len(stones)

def parse_input(data):
    occurances = {}
    for val in data:
        if val not in occurances:
            occurances[val] = 1
            continue
        occurances[val] += 1
    return occurances

def blink_dict(stones_before_blink):
    stones_after_blink = {}
    for stone,count in stones_before_blink.items():
        if stone == '0':
            if '1' in stones_after_blink:
                stones_after_blink['1'] += count
            else:
                stones_after_blink['1'] = count
            continue
        stone_size = len(stone)
        if stone_size%2 == 0:
            first_stone = stone[:stone_size//2]
            second_stone = str(int(stone[stone_size//2:]))
            if first_stone in stones_after_blink: 
                stones_after_blink[first_stone] += count
            else:
                stones_after_blink[first_stone] = count
            if second_stone  in stones_after_blink:
                stones_after_blink[second_stone] += count
            else:
                stones_after_blink[second_stone] = count
            continue
        new_stone = str(int(stone)*2024)
        if new_stone in stones_after_blink:
            stones_after_blink[new_stone] += count
        else:
            stones_after_blink[new_stone] = count
    return stones_after_blink

def count_stones_dict(stones,nr_blinks):
    for i in range(nr_blinks):
        stones = blink_dict(stones)
    return sum(count for _,count in stones.items())
    
if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    stones = read_input(file_name)
    stones = parse_input(stones)
    print(f"Answer to day 11 part 1: {count_stones_dict(stones,25)}")
    print(f"Answer to day 11 part 2: {count_stones_dict(stones,75)}")