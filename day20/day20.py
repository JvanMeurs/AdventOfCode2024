import heapq

def parse_input(file_name):
    with open(file_name,'r') as input_file:
        lines = input_file.readlines()

    grid = {}
    for r,line in enumerate(lines):
        line = line.strip()
        nr_cols = len(line)
        for c in range(nr_cols):
            if line[c] != "#":
                grid[(r,c)] = 10**18
                if line[c] == "S":
                    start = (r,c)
                if line[c] == "E":
                    destination = (r,c)    
        nr_rows = r+1

    return grid,start,destination,nr_rows,nr_cols

def heuristic(a, b):
    """
    Heuristic function to estimate the cost from current node 'a' to destination node 'b'.
    Using Manhattan distance as the heuristic.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

directions = [(1,0),(-1,0),(0,1),(0,-1)]
def find_shortest_path(grid, start, destination):
    pq = [] 
    heapq.heappush(pq, (0 + heuristic(start, destination), 0, start)) 

    grid[start] = 0

    while pq:
        f, g, current = heapq.heappop(pq)
        
        if current == destination:
            return g 

        r, c = current

        for dr, dc in directions: 
            neighbor = (r + dr, c + dc)

            if neighbor in grid and grid[neighbor] is not None:
                new_cost = g + 1 
                
                if neighbor not in grid or new_cost < grid[neighbor]:
                    grid[neighbor] = new_cost
                    f = new_cost + heuristic(neighbor, destination)
                    heapq.heappush(pq, (f, new_cost, neighbor))
    return -1

cheats = [(2,0),(-2,0),(0,2),(0,-2)]
def cheat(grid,gain_margin):
    time_saving = {}

    for current in grid.keys():
        r, c = current
        for dr, dc in cheats: 
            neighbor = (r + dr, c + dc)

            if neighbor in grid:
                saved_time = grid[neighbor] - grid[current] - 2
                if saved_time >= gain_margin:
                    if saved_time in time_saving:
                        time_saving[saved_time] += 1
                    else:
                        time_saving[saved_time] = 1
    return sum(time_saving.values())

def main(file_name, gain_margin, text):
    grid,start,destination,nr_rows,nr_cols = parse_input(file_name)
    shortest_path_cost = find_shortest_path(grid, start, destination)
    time_saving = cheat(grid,gain_margin)
    print(f"{text} cost without cheating: {shortest_path_cost}")
    print(f"{text} time saving: {time_saving}")


if __name__ == ("__main__"): # pragma: no cover
    main(file_name= "example1", gain_margin=2, text="Example 1")
    main(file_name="input", gain_margin=100, text = "Day 20 part 1")
