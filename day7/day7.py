# day 7 Advent of Code
def read_diagram(file_path):
    tachyon_manifold ={
        "Max_rows" : 0,
        "Max_cols" : 0,
        "laser_start" : 0,
        "diagram" : [],
        "splitter" : "^"
    }

    with open(file_path, "r") as AOC:
        for line in AOC:
            line = list(line.strip())
            tachyon_manifold["diagram"].append(line)
        
        tachyon_manifold["Max_cols"] = len(line)
    
    tachyon_manifold["Max_rows"] = len(tachyon_manifold["diagram"])

    for index, space in enumerate(tachyon_manifold["diagram"][0]):
        if space == "S":
            tachyon_manifold["laser_start"] = index

    return tachyon_manifold

def look_for_splitters(tachyon_manifold):
    splitter_count = 0
    splitter_missed = 0
    laser_beams = []
    laser_beams.append(tachyon_manifold["laser_start"])
    for r_index, row in enumerate(tachyon_manifold["diagram"]):
        for c_index, col in enumerate(row):
            if col == "^":
                if c_index in laser_beams:
                    splitter_count += 1
                    new_beams = found_splitter(r_index, c_index, tachyon_manifold["Max_rows"], tachyon_manifold["Max_cols"], laser_beams)
                    old_laser = laser_beams.index(c_index)
                    laser_beams.pop(old_laser)
                    laser_beams.extend(new_beams)
                else:
                    splitter_missed += 1
    
    print(f"splitters used:{splitter_count} - Splitters Missed:{splitter_count}")


def found_splitter(row, col, max_rows, max_cols, laser_beams):
    new_beams = []
    if col in laser_beams:
        if col + 1 <= max_cols:
            new_laser = col + 1
            if new_laser not in laser_beams:
                new_beams.append(new_laser)
        
        if col - 1 >= 0:
            new_laser = col -1
            if new_laser not in laser_beams:
                new_beams.append(new_laser)
    
    return new_beams


class Laser_beam:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.split_left = 0
        self.split_right = 0
    
    def __repr__(self):
        return f"laser Node at {self.value}"
    
the_tachyon_manifold = {}


def check_next(node, the_drawing):
    next_spliter = []
    for direction in [node.split_left, node.split_right]:
        for down_num in range(node.value[0], the_drawing["Max_cols"]):
            going_down = the_drawing['diagram'][down_num][direction]
            if going_down == "^":
                found_next = down_num
                next_spliter.append((found_next, direction))
                break
    
    
    return next_spliter


def get_manifold_data(the_drawing):
    for r_index, row in enumerate(the_drawing["diagram"]):
        for c_index, col in enumerate(row):
            if col == "^":
                the_tachyon_manifold[(r_index, c_index)] = Laser_beam((r_index, c_index))
                the_tachyon_manifold[(r_index, c_index)].split_left = c_index - 1
                the_tachyon_manifold[(r_index, c_index)].split_right = c_index + 1
    
    for (r_index, c_index), node in the_tachyon_manifold.items():
        next_ones = check_next(node, the_drawing)

        for n_one in next_ones:
            if n_one in the_tachyon_manifold:
                the_tachyon_manifold[r_index, c_index].children.append(the_tachyon_manifold[n_one])

    print("done !")

def get_paths(tachyon_pos, travelled):
    travelled.append(tachyon_pos)

    if len(tachyon_pos.children) < 1:
        #print(travelled)
        travelled.pop()
        # return 2 to count the last split
        return 2
    
    total = 0
    if len(tachyon_pos.children) == 1:
        total += 1
        total += get_paths(tachyon_pos.children[0], travelled)
    else:
        for laser in tachyon_pos.children:
            total += get_paths(laser, travelled)
        
    travelled.pop()
    return total

if __name__ == "__main__":
    print("Advent of Code 2025 Day 7")

    TEST = r"day7\test_input.txt"
    REAL = r"day7\puzzle_input.txt"

    diagram = read_diagram(REAL)

    #look_for_splitters(diagram)

    get_manifold_data(diagram)
    
    total = get_paths(the_tachyon_manifold[(2,70)], [])

    print(total)