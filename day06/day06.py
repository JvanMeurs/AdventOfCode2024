def turn_90(old_direction):
    match old_direction:
        case 0 | 1 | 2:
            new_direction = old_direction + 1
        case _:
            new_direction = 0
    return new_direction

def walk(direction,old_point):
    match direction:
        case 0:
            new_point = (old_point[0],old_point[1]-1)
        case 1:
            new_point = (old_point[0]+1,old_point[1])
        case 2:
            new_point = (old_point[0],old_point[1]+1)
        case 3:
            new_point = (old_point[0]-1,old_point[1])
    return new_point


def check_loop(grid,point,direction):
    return get_bit(grid[point],direction)


def visited_tiles(grid,point,direction):    
    while True:
        new_point = walk(direction,point)
        if new_point not in grid.keys():
            return grid,0
        if grid[new_point] is not None:
            if check_loop(grid,new_point,direction):
                return grid,1
            point = new_point
            grid[point] = set_bit(grid[point],direction)
            continue
        direction = turn_90(direction)
        grid[point] = set_bit(grid[point],direction)

def filter_visited_points(grid):
    visited_points = []
    for point,value in grid.items():
        if value is not None and value > 0:
            visited_points.append(point)

    return visited_points

def loop_obstacle_positions(grid, start_point,start_direction,visited_points):
    nr_loops = 0
    for visited_point in visited_points:
        if visited_point == start_point:
            continue
        
        grid_copy = grid.copy()
        grid_copy[visited_point] = None
        _, isLoop = visited_tiles(grid_copy,start_point,start_direction)
        nr_loops += isLoop

    return nr_loops

def parse_input_dict(file_name):
    with open(file_name,'r') as input:
        data = input.read().strip().splitlines()

    grid = {}
    for y,line in enumerate(data):
        for x in range(len(line)):
            match line[x]:
                case "#":
                    T = None
                case "^":
                    T = 0b1
                    start_point = (x,y)
                    start_direction = 0
                case ">":
                    T = 0b10
                    start_point = (x,y)
                    start_direction = 1
                case "v":
                    T = 0b100
                    start_point = (x,y)
                    start_direction = 2
                case "<":
                    T = 0b1000
                    start_point = (x,y)
                    start_direction = 3
                case _:
                    T = 0
            grid.update({(x,y): T})

    return grid, start_point, start_direction

def set_bit(value,bit):
    return value | (1 << bit)

def get_bit(value,bit):
    return value & (1 << bit)


if __name__ == ("__main__"):
    
    grid, start_point, start_direction = parse_input_dict("sample_input.txt")
    grid_copy = grid.copy()
    grid_copy,_ = visited_tiles(grid_copy, start_point, start_direction)
    visited_points = filter_visited_points(grid_copy)
    print(f"Answer day 6 part 1 from sample input: {len(visited_points)}")

    nr_loops = loop_obstacle_positions(grid,start_point,start_direction,visited_points)
    print(f"Answer day 6 part 2 from sample input: {nr_loops}")

    grid, start_point, start_direction = parse_input_dict("input.txt")
    grid_copy = grid.copy()
    grid_copy,_ = visited_tiles(grid_copy, start_point, start_direction)
    visited_points = filter_visited_points(grid_copy)
    print(f"Answer day 6 part 1 from input: {len(visited_points)}")

    nr_loops = loop_obstacle_positions(grid,start_point,start_direction,visited_points)
    print(f"Answer day 6 part 2 from input: {nr_loops}")

