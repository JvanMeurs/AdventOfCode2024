import numpy as np

def parse_input(file_name):

    with open(file_name, 'r') as file:
        lines = file.read().strip().split('\n')

    grid = [list(line) for line in lines]

    return np.array(grid)

def turn_90(old_direction):

    match old_direction:
        case "^":
            new_direction = ">"
        case ">":
            new_direction = "v"
        case "v":
            new_direction = "<"
        case "<":
            new_direction = "^"
    
    return new_direction

def walk(direction,x,y):
    match direction:
        case "^":
            new_x = x
            new_y = y-1
        case ">":
            new_x = x+1
            new_y = y
        case "v":
            new_x = x
            new_y = y+1
        case "<":
            new_x = x-1
            new_y = y
    return new_x,new_y

def check_collision(map,x,y):
    return map[y,x] == "#"

def check_out_of_bounds(map,x,y):
    max_y, max_x = map.shape
    return x < 0 or x >= max_x or y < 0 or y >= max_y

def check_loop(map,x,y,direction):
    return map[y,x] == direction


def visited_tiles(map):    
    x,y,direction = find_start(map)
    x_og,y_og,d_og = find_start(map)

    while True:
        new_x, new_y = walk(direction,x,y)
        if check_out_of_bounds(map,new_x,new_y):
            return map,0
        if check_loop(map,new_x,new_y,direction):
            return map,1
        if not check_collision(map,new_x,new_y):
            x,y = new_x, new_y
            map[y,x] = direction
            continue
        direction = turn_90(direction)

def find_start(map):
    guard = ["<",">","^","v"]

    for i,direction in enumerate(guard):
        y,x = np.where(map == direction)
        if x.size != 0:
            return x, y, direction

def count_visited_tiles(map):
    x=np.array([])
    y=np.array([])
    
    for i in ["<",">","^","v"]:
        temp = np.where(map == i)
        x = np.concatenate((x,temp[1]))
        y = np.concatenate((y,temp[0]))       
    
    return x.size, x, y

def set_obstacle(map,x,y):
    new_map = map
    x_og, y_og, _ = find_start(new_map)
    if not(x == x_og and y == y_og):
        new_map[y,x] = "#"
    return new_map

def loop_obstacle_positions(map, x, y):
    print(f"Size = {map.shape}")
    nr_loops = 0
    for i in range(x.size):
        print(f"i,x,y = {i, x[i],y[i]}")
        tainted_map = set_obstacle(map.copy(),np.int16(x[i]),np.int16(y[i]))
        tainted_map, isLoop = visited_tiles(tainted_map)
        nr_loops += isLoop

    return nr_loops

if __name__ == ("__main__"):
    map = parse_input("input.txt")
    visited_map = visited_tiles(map.copy())
    nr_visited_tiles,x,y = count_visited_tiles(visited_map[0])

    print(loop_obstacle_positions(map.copy(),x,y))

    # map = parse_input("input.txt")
    # visited_map = visited_tiles(map)
    # print(count_visited_tiles(visited_map))