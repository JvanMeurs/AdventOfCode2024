import heapq

directions = [(-1,0),(0,-1),(1,0),(0,1)]
    
def parse_input(file_name):
    with open(file_name,'r') as input_file:
        return input_file.read().strip().split('\n')

def define_grid(data,nr_rows,nr_cols,nr_bytes):
    grid = {(r,c) : 10**18 for r in range(nr_rows) for c in range(nr_cols)}
    
    [grid.__setitem__((r, c), None) for r in [-1, nr_rows] for c in range(nr_cols)]
    [grid.__setitem__((r, c), None) for r in range(nr_rows) for c in [-1, nr_cols]]
    
    grid,_,_ = corrupt_grid(data,grid,0,nr_bytes)
    return grid

def corrupt_grid(data,grid,start_byte,nr_bytes):
    for i in range(start_byte,start_byte+nr_bytes):
        r,c = tuple(map(int,data[i].split(",")))
        grid[(r,c)] = None
    return grid,r,c


def heuristic(a, b):
    """
    Heuristic function to estimate the cost from current node 'a' to destination node 'b'.
    Using Manhattan distance as the heuristic.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_shortest_path(grid, start, destination):
    pq = [] 
    heapq.heappush(pq, (0 + heuristic(start, destination), 0, start)) 

    costs = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)
        
        if current == destination:
            return g 

        r, c = current

        for dr, dc in directions: 
            neighbor = (r + dr, c + dc)

            if neighbor in grid and grid[neighbor] is not None:
                new_cost = g + 1 
                
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    f = new_cost + heuristic(neighbor, destination)
                    heapq.heappush(pq, (f, new_cost, neighbor))
    return -1

def print_grid(grid,nr_rows,nr_cols):
    for r in range(nr_rows):
        row = ""
        for c in range(nr_cols):
            row = f"{row}{"#" if grid[(r,c)] is None else "." if grid[(r,c)] == 10**18 else "~"}"
        print(row)
    print()

def check_if_corrupted(data,grid,nr_rows,nr_cols,nr_bytes,path_count):
    while path_count != -1:
        grid,r,c = corrupt_grid(data,grid,nr_bytes,1) 
        path_count = find_shortest_path(grid,(0,0),(nr_rows-1,nr_cols-1))
        nr_bytes+=1
    return r,c

if __name__ == ("__main__"): # pragma: no cover
    file_name = "example1"
    nr_rows = 7
    nr_cols = 7
    nr_bytes = 12
    data = parse_input(file_name)
    grid = define_grid(data,nr_rows,nr_cols,nr_bytes)
    print_grid(grid,nr_rows,nr_cols)
    path_count = find_shortest_path(grid,(0,0),(nr_rows-1,nr_cols-1))
    print(f"Example 1 minimum number of steps: {path_count}")
    r,c = check_if_corrupted(data,grid,nr_rows,nr_cols,nr_bytes,path_count)
    print(f"Example 1 corrupted data at: {r},{c}")



    file_name = "input"
    nr_rows = 71
    nr_cols = 71
    nr_bytes = 1024
    data = parse_input(file_name)
    grid = define_grid(data,nr_rows,nr_cols,nr_bytes)    
    path_count = find_shortest_path(grid,(0,0),(nr_rows-1,nr_cols-1))
    print(f"Answer day18 part 1: {path_count}")
    r,c = check_if_corrupted(data,grid,nr_rows,nr_cols,nr_bytes,path_count)
    print(f"Answer day18 part 2: {r},{c}")