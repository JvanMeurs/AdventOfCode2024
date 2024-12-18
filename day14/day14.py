import re

def parse_input(file_name):
    with open(file_name,'r') as input_file:
        lines = input_file.readlines()

    data = {}
    for i,line in enumerate(lines):
        digits = re.findall(r'[-]?\d+', line)
        data[i] = {"pos":(int(digits[0]),int(digits[1])), "vel" :(int(digits[2]),int(digits[3]))}
    return data

def update_pos(next_pos_dict,cur,max_x,max_y):
    if cur["pos"] in next_pos_dict:
        if cur["vel"] in next_pos_dict[cur["pos"]]:
            cur["pos"] = next_pos_dict[cur["pos"]][cur["vel"]]
            return next_pos_dict, cur
        else:
            new_pos = next_pos(cur,max_x,max_y)
            next_pos_dict[cur["pos"]][cur["vel"]] = new_pos
            cur["pos"] = new_pos
            return next_pos_dict, cur
    else:
        new_pos = next_pos(cur,max_x,max_y)
        next_pos_dict[cur["pos"]] = {cur["vel"] : new_pos}
        cur["pos"] = new_pos
        return next_pos_dict, cur
        
def next_pos(cur,max_x,max_y):
    x,y = cur["pos"]
    dx,dy = cur["vel"]

    nx = x+dx
    if nx < 0: nx += max_x
    if nx >= max_x: nx -= max_x

    ny = y+dy
    if ny < 0: ny += max_y
    if ny >= max_y: ny -= max_y
    
    return (nx,ny)

def loop_data(next_pos_dict, data, nr_secs, max_x, max_y):
    best_distance = 10**18
    best_distance_i = -1
    for i in range(nr_secs):
        new_distance = total_distance_sum(data)
        if new_distance < best_distance:
            best_distance = new_distance
            best_distance_i = i
            print_grid(data,max_x,max_y,i)
        for robot in data.keys():
            next_pos_dict,data[robot] = update_pos(next_pos_dict,data[robot],max_x,max_y)
    return data,best_distance,best_distance_i

def get_safety_score_per_quadrant(data,max_x,max_y):
    middle_x = max_x//2
    middle_y = max_y//2

    q1_robots,q2_robots,q3_robots,q4_robots = 0,0,0,0

    for robot in data.keys():
        x,y = data[robot]["pos"]
        if x < middle_x:
            if y < middle_y:
                q1_robots += 1
            if y > middle_y:
                q3_robots += 1
        if x > middle_x:
            if y < middle_y:
                q2_robots += 1
            if y > middle_y:
                q4_robots += 1
    return q1_robots,q2_robots,q3_robots,q4_robots

def get_safety_score(q1_robots,q2_robots,q3_robots,q4_robots):
    return q1_robots*q2_robots*q3_robots*q4_robots

def print_grid(data,max_x,max_y,i):
    grid = [[None for _ in range(max_x)] for _ in range(max_y)]
    for x in range(max_x):
        for y in range(max_y):
            for _,robot in data.items():
                if robot["pos"] == (x,y):
                    grid[y][x] = ("x")

            if grid[y][x] is None:
                grid[y][x] = (".")

    with open("christmastree.txt",'w') as grid_file:
        print(i,file=grid_file)
        for line in grid:
            print("".join(line),file=grid_file)

def distance_sum (arr, n):     
    arr.sort()
     
    res = 0
    sum = 0
    for i in range(n):
        res += (arr[i] * i - sum)
        sum += arr[i]
     
    return res
     
def total_distance_sum( data ):
    x = []
    y = []
    n = len(data)
    for robot in data.keys():
        x.append(data[robot]["pos"][0])
        y.append(data[robot]["pos"][1])
    return distance_sum(x, n) + distance_sum(y, n)

if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    data = parse_input(file_name)
    max_x = 101
    max_y = 103
    nr_secs=100
    next_pos_dict = {}

    data,_,_ = loop_data(next_pos_dict, data, nr_secs, max_x, max_y)
    q1_robots,q2_robots,q3_robots,q4_robots = get_safety_score_per_quadrant(data,max_x,max_y)
    
    print(f"Answer day 14 part 1: {get_safety_score(q1_robots,q2_robots,q3_robots,q4_robots)}")

    data = parse_input(file_name)
    nr_secs=10000
    data,best_distance,best_distance_i = loop_data(next_pos_dict, data, nr_secs, max_x, max_y)
    print(f"Answer day 14 part 2 is possibly: {best_distance_i} with a distance of {best_distance}")
    