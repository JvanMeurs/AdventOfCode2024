def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip().split('\n')

def traverse_grid(grid):
    
    grid = [list(row) for row in grid]
    nr_rows = len(grid)
    nr_cols = len(grid[0])

    visited_global = [[False] * nr_cols for _ in range(nr_rows)]

    adjacency = [(1,0), (-1,0), (0,1), (0,-1)]
    def dfs_rec(visited, curr_row, curr_col):
        
        area = 1
        perimiter = 0
        sides = 4
        for delta_row, delta_col in adjacency:
            new_row, new_col = curr_row + delta_row, curr_col + delta_col
            if 0 <= new_row < nr_rows and 0 <= new_col < nr_cols:
                if not visited[new_row][new_col]:
                    if grid[new_row][new_col] == grid[curr_row][curr_col]:
                        visited[new_row][new_col] = True
                        visited_global[new_row][new_col] = True
                        a,p = dfs_rec(visited, new_row, new_col)
                        area += a
                        perimiter += p
                    else:
                        perimiter += 1
            else:
                perimiter += 1

        return area,perimiter
                
    def dfs(start_row, start_col):
        visited = [[False] * nr_cols for _ in range(nr_rows)]
        visited[start_row][start_col] = True
        visited_global[start_row][start_col] = True
        return dfs_rec(visited, start_row, start_col)

    plants = {}
    for r in range(nr_rows):
        for c in range(nr_cols):
            if not visited_global[r][c]:
                total_area,total_perimiter = dfs(r,c)
                plants[len(plants)]={"area": total_area, "perimiter":total_perimiter}

    return plants

def calculate_total_cost(plants):
    return sum(plants[key]["area"]*plants[key]["perimiter"] for key in plants.keys())

if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs = calculate_total_cost(plants)
    print(f"Answer to day 12 part 1: {costs}")
    