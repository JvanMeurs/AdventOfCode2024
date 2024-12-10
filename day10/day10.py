from collections import deque

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip().split('\n')

def count_trailhead_scores(grid):
    
    grid = [list(map(int, row)) for row in grid]
    nr_rows = len(grid)
    nr_cols = len(grid[0])

    trailhead_positions = []
    for r in range(nr_rows):
        for c in range(nr_cols):
            if grid[r][c] == 0:
                trailhead_positions.append((r,c))

    adjacency = [(1,0), (-1,0), (0,1), (0,-1)]

    def bfs(start_row, start_col):
        trailhead_score = 0
        queue = deque([(start_row,start_col)])
        visited = [[False] * nr_cols for _ in range(nr_rows)]
        visited[start_row][start_col] = True

        while queue:
            (curr_row,curr_col) = queue.popleft()

            for y,x in adjacency:
                new_row = curr_row + y
                new_col = curr_col + x 
                if 0 <= new_row < nr_rows and 0 <= new_col < nr_cols and not visited[new_row][new_col]:
                    if grid[new_row][new_col] == grid[curr_row][curr_col] + 1:
                        visited[new_row][new_col] = True
                        queue.append((new_row,new_col))

                        if grid[new_row][new_col] == 9:
                            trailhead_score += 1

        return trailhead_score
    
    def dfs_rec(visited, curr_row, curr_col):
        if grid[curr_row][curr_col] == 9:
            return 1
        
        path_count = 0

        for delta_row, delta_col in adjacency:
            new_row, new_col = curr_row + delta_row, curr_col + delta_col
            if 0 <= new_row < nr_rows and 0 <= new_col < nr_cols and not visited[new_row][new_col]:
                if grid[new_row][new_col] == grid[curr_row][curr_col] + 1:
                    visited[curr_row][curr_col] = True
                    path_count += dfs_rec(visited, new_row, new_col)
                    visited[curr_row][curr_col] = False

        return path_count
                
    def dfs(start_row, start_col):
        visited = [[False] * nr_cols for _ in range(nr_rows)]
        visited[start_row][start_col] = True
        return dfs_rec(visited, start_row, start_col)

    trailhead_scores = 0
    trailhead_ratings = 0
    for th_row,th_col in trailhead_positions:
        trailhead_scores += bfs(th_row,th_col)
        trailhead_ratings += dfs(th_row, th_col)

    return trailhead_scores,trailhead_ratings

if __name__ == ("__main__"):
    file_name = "sample_input"
    grid = read_input(file_name)
    trailhead_scores,trailhead_ratings = count_trailhead_scores(grid)
    print(f"Day 10 part 1 answer from {file_name}: {trailhead_scores}")
    print(f"Day 10 part 2 answer from {file_name}: {trailhead_ratings}")
    
    file_name = "input"
    grid = read_input(file_name)
    trailhead_scores,trailhead_ratings = count_trailhead_scores(grid)
    print(f"Day 10 part 1 answer from {file_name}: {trailhead_scores}")
    print(f"Day 10 part 2 answer from {file_name}: {trailhead_ratings}")
    

