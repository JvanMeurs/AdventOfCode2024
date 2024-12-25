import heapq

directions = ["^","v","<",">"]
class node():
    def __init__(self,point,up,down,left,right):
        self.point = point
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.__determine_cost()

    def __determine_cost(self):
        self.cost_up =      {"^": 1    if self.up    else None,
                             "v": 2001 if self.down  else None,
                             "<": 1001 if self.left  else None,
                             ">": 1001 if self.right  else None}
        self.cost_down =    {"^": 2001 if self.up    else None,
                             "v": 1    if self.down  else None,
                             "<": 1001 if self.left  else None,
                             ">": 1001 if self.right  else None}
        self.cost_left =    {"^": 1001 if self.up    else None,
                             "v": 1001 if self.down  else None,
                             "<": 1    if self.left  else None,
                             ">": 2001 if self.right else None}
        self.cost_right =   {"^": 1001 if self.up    else None,
                             "v": 1001 if self.down  else None,
                             "<": 2001 if self.left  else None,
                             ">": 1    if self.right  else None}

    def get_cost(self,direction):
        if direction == "^":
            return self.cost_up
        if direction == "v":
            return self.cost_down
        if direction == "<":
            return self.cost_left
        if direction == ">":
            return self.cost_right
        return None
    
def parse_input(file_name):
    with open(file_name,'r') as input_file:
        lines = input_file.readlines()

    grid = {}
    for r,line in enumerate(lines):
        line = line.strip()
        nr_cols = len(line)
        for c in range(nr_cols):
            if line[c] != "#":
                grid[(r,c)] = node(point = (r,c),
                                   up    = None if lines[r-1][c] == "#" else (r-1,c),
                                   down  = None if lines[r+1][c] == "#" else (r+1,c),
                                   left  = None if lines[r][c-1] == "#" else (r,c-1),
                                   right = None if lines[r][c+1] == "#" else (r,c+1))
                if line[c] == "S":
                    start = (r,c)
                if line[c] == "E":
                    destination = (r,c)    
        nr_rows = r+1

    return grid,start,destination,nr_rows,nr_cols

def find_shortest_path(grid, start, destination):
    pq = []
    heapq.heappush(pq, (0, start, ">")) 

    visited = {}

    while pq:
        cost, current, direction = heapq.heappop(pq)

        if (current,direction) in visited and visited[(current,direction)] < cost:
            continue

        visited[(current,direction)] = cost

        cur_node = grid[current]

        for dir_idx, neighbor in enumerate([cur_node.up, cur_node.down, cur_node.left, cur_node.right]):
            if neighbor is not None:
                next_direction = directions[dir_idx]
                movement_cost = cur_node.get_cost(direction)[next_direction]
                if movement_cost is not None:
                    heapq.heappush(pq, (cost + movement_cost, neighbor, next_direction))
    
    min_sum = -1
    for d in directions:
        if (destination,d) in visited:
            if min_sum == -1 or min_sum > visited[(destination,d)]:
                min_sum = visited[(destination,d)]
                end = (destination,d)
    return min_sum, visited, end

def nr_unique_points_on_shortest_routes(visited,cur):
    visited_points = set()
    
    def backtrack_path(visited,cur,visited_points):
        (r,c),direction = cur
        visited_points.add((r,c))
        if direction == "^":
            pre_point = (r+1,c)
        if direction == "v":
            pre_point = (r-1,c)
        if direction == ">":
            pre_point = (r,c-1)
        if direction == "<":
            pre_point = (r,c+1)
        for d in directions:
            if (pre_point,d) in visited and (visited[(pre_point,d)] == visited[cur] - 1 or visited[(pre_point,d)] == visited[cur] - 1001):
                visited_points = backtrack_path(visited,(pre_point,d),visited_points)
        return visited_points
    
    visited_points = backtrack_path(visited,cur,visited_points)

    return len(visited_points)

if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    grid,start,destination,nr_rows,nr_cols = parse_input(file_name)
    shortest_path_cost,visited,end = find_shortest_path(grid, start, destination)
    path_count = nr_unique_points_on_shortest_routes(visited,end)
    print(f"Answer to day 16 part 1: {shortest_path_cost}")
    print(f"Answer to day 16 part 2: {path_count}")