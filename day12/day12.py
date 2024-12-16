def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip().split('\n')

def traverse_grid(grid):
    
    grid = [list(row) for row in grid]
    nr_rows = len(grid)
    nr_cols = len(grid[0])

    visited_global = [[False] * nr_cols for _ in range(nr_rows)]
    
    adjacency = [(1,0), (-1,0), (0,1), (0,-1)]
    relative_vertices = [(0,0), (1,0), (0,1), (1,1)]

    def fill_vertices(vertices, curr_row,curr_col):
        for delta_vrow, delta_vcol in relative_vertices:
            key = (curr_row+delta_vrow,curr_col+delta_vcol)
            if key in vertices:
                vertices[key] += 1
            else:
                vertices[key] = 1
        return vertices
    
    def dfs_rec(visited, curr_row, curr_col,vertices):
        
        vertices = fill_vertices(vertices, curr_row,curr_col)

        area = 1
        perimeter = 0
        for delta_row, delta_col in adjacency:
            new_row, new_col = curr_row + delta_row, curr_col + delta_col
            if inbounds(new_row, nr_rows) and inbounds(new_col, nr_cols):
                if not visited[new_row][new_col]:
                    if grid[new_row][new_col] == grid[curr_row][curr_col]:
                        visited[new_row][new_col] = True
                        visited_global[new_row][new_col] = True
                        a,p,vertices  = dfs_rec(visited, new_row, new_col,vertices)
                        area += a
                        perimeter += p
                    else:
                        perimeter += 1
            else:
                perimeter += 1

        return area,perimeter,vertices
                
    def dfs(start_row, start_col):
        visited = [[False] * nr_cols for _ in range(nr_rows)]
        visited[start_row][start_col] = True
        vertices = {}
        visited_global[start_row][start_col] = True
        return dfs_rec(visited, start_row, start_col, vertices),visited

    plants = {}
    for r in range(nr_rows):
        for c in range(nr_cols):
            if not visited_global[r][c]:
                (total_area,total_perimeter,vertices),visited = dfs(r,c)
                sides = 0
                for vertex,count in vertices.items():
                    sides += count%2
                    if count == 2:
                        row,col = vertex
                        if (inbounds(row - 1,nr_rows)     and 
                            inbounds(col - 1,nr_cols)     and 
                            inbounds(row,    nr_rows)     and 
                            inbounds(col,    nr_cols)     and 
                            not visited[row - 1][col - 1] and 
                            not visited[row][col]):
                                sides += 2
                        if (inbounds(row - 1,nr_rows) and 
                            inbounds(col    ,nr_cols) and 
                            inbounds(row    ,nr_rows) and 
                            inbounds(col - 1,nr_cols) and 
                            not visited[row - 1][col] and 
                            not visited[row][col-1]):
                                sides += 2

                plants[len(plants)]={"area": total_area, "perimeter":total_perimeter,"sides": sides}
    return plants

def inbounds(i,imax):
    return 0 <= i < imax

def calculate_total_cost(plants):
    costs = 0
    bulk_costs = 0
    for key in plants.keys():
        costs += plants[key]["area"]*plants[key]["perimeter"]
        bulk_costs += plants[key]["area"]*plants[key]["sides"]
    return costs,bulk_costs

if __name__ == ("__main__"): # pragma: no cover
    file_name = "input"
    data = read_input(file_name)
    plants = traverse_grid(data)
    costs, bulk_costs = calculate_total_cost(plants)
    print(f"Answer to day 12 part 1: {costs}")
    print(f"Answer to day 12 part 2: {bulk_costs}")
    