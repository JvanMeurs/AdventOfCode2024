def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip().split('\n')

def get_grid_points(data):
    grid_points = set()
    frequenct_dict = dict()
    max_y = len(data)
    max_x = len(data[0])
    for y,line in enumerate(data):
        for x in range(max_x):
            grid_points.add((x,y))
            frequenct_dict = get_frequency_points(frequenct_dict,line[x],x,y)
    return grid_points, frequenct_dict, (max_x,max_y)


def get_frequency_points(frequency_dict,value,x,y):
    if not value == ".":
        if value not in frequency_dict.keys():
            frequency_dict[value] = [(x,y)]
        else:
            frequency_dict[value].append((x,y))
    return frequency_dict

def get_focus_points(frequency_dict,focus_rule,max_point=None):
    focus_points = set()
    for _,points in frequency_dict.items():
        for i,point in enumerate(points):
            for j in range(len(points[i+1:])):
                focus_points = focus_rule(focus_points,point,points[j+i+1],max_point)
    return focus_points

def focus_rule_1(focus_points, point,next_point,*argv):
    delta = subtract_points(point, next_point)
    focus_points.add(add_points(point, delta))
    focus_points.add(subtract_points(next_point,delta))
    return focus_points

def focus_rule_2(focus_points, point,next_point,max_point):
    delta = subtract_points(point, next_point)

    new_focus_point = point
    while point_in_bounds(new_focus_point,max_point):
        focus_points.add(new_focus_point)
        new_focus_point = add_points(new_focus_point, delta)
    
    new_focus_point = next_point
    while point_in_bounds(new_focus_point,max_point):
        focus_points.add(new_focus_point)
        new_focus_point = subtract_points(new_focus_point, delta)

    return focus_points

def point_in_bounds(point,max_point):
    return point[0] >= 0 and point[0] <= max_point[0] and point[1] >= 0 and point[1] <= max_point[1] 

def subtract_points(a,b):
    return (a[0] - b[0], a[1] - b[1])

def add_points(a,b):
    return (a[0] + b[0], a[1] + b[1])

def get_unique_focus_points(grid_points,focus_points):
    return len(focus_points.intersection(grid_points))

if __name__ == ("__main__"):
    data = read_input("sample_input")
    grid_points, frequency_dict, max_point = get_grid_points(data)
    focus_points = get_focus_points(frequency_dict,focus_rule_1)
    nr_unique_focus_points = get_unique_focus_points(grid_points,focus_points)
    print(f"Answer part 1 from sample input: {nr_unique_focus_points}")

    focus_points = get_focus_points(frequency_dict,focus_rule_2,max_point)
    nr_unique_focus_points = get_unique_focus_points(grid_points,focus_points)
    print(f"Answer part 2 from sample input: {nr_unique_focus_points}")

    data = read_input("input")
    grid_points, frequency_dict, max_point = get_grid_points(data)
    focus_points = get_focus_points(frequency_dict,focus_rule_1)
    nr_unique_focus_points = get_unique_focus_points(grid_points,focus_points)
    print(f"Answer part 1 from input: {nr_unique_focus_points}")

    focus_points = get_focus_points(frequency_dict,focus_rule_2,max_point)
    nr_unique_focus_points = get_unique_focus_points(grid_points,focus_points)
    print(f"Answer part 29 from input: {nr_unique_focus_points}")