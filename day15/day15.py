def parse_input(file_name):
    with open(file_name,'r') as input_file:
        lines = input_file.readlines()

    grid = {}
    instructions = []

    is_grid = True
    for r,line in enumerate(lines):
        line = line.strip()
        if line == "":
            is_grid = False
            continue
        if is_grid:
            nr_cols = len(line)
            for c in range(nr_cols):
                grid[(r,c)] = None if line[c] == "#" else line[c]
                if line[c] == "@":
                    robot_loc = (r,c)
            nr_rows = r+1
            continue
        instructions.append(line)
    
    instructions = "".join(instructions)

    return grid,instructions,robot_loc,nr_rows,nr_cols


movement = {"<": (0,-1), ">": (0,1), "v": (1,0), "^": (-1,0)}
def follow_instructions(grid,instructions,robot_loc):
    cr,cc = robot_loc
    for instruction in instructions:
        dr,dc = movement[instruction]
        grid = rec_instruction(grid,cr,cc,dr,dc)
        cr,cc = list(grid.keys())[list(grid.values()).index("@")]
    return grid
            
def rec_instruction(grid,r,c,dr,dc):
    if grid[(r+dr,c+dc)] is None:
        return grid
    if grid[(r+dr,c+dc)] == "O":
        grid = rec_instruction(grid,r+dr,c+dc,dr,dc)
    if grid[(r+dr,c+dc)] == ".":
        grid[(r+dr,c+dc)] = grid[(r,c)]
        grid[(r,c)] = "."
    return grid
    
def print_grid(grid,nr_rows,nr_cols):
    for r in range(nr_rows):
        row = ""
        for c in range(nr_cols):
            row = f"{row}{"#" if grid[(r,c)] is None else grid[(r,c)]}"
        print(row)

def determine_gps_coordinates(grid):
    coordinate_sum = 0
    for key in grid.keys():
        if grid[key] == "O":
            r,c = key
            coordinate_sum += 100*r + c
    return coordinate_sum

if __name__ == ("__main__"): # pragma: no cover
    file_name = "Input"
    grid,instructions,robot_loc,nr_rows,nr_cols = parse_input(file_name)
    grid = follow_instructions(grid,instructions,robot_loc)
    # print_grid(grid,nr_rows,nr_cols)
    coordinate_sum = determine_gps_coordinates(grid)

    print(f"Answer to day 15 part 1 is: {coordinate_sum}")

