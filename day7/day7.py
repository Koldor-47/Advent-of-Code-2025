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


if __name__ == "__main__":
    print("Advent of Code 2025 Day 7")

    TEST = r"day7\test_input.txt"
    REAL = r"day7\puzzle_input.txt"

    diagram = read_diagram(REAL)

    look_for_splitters(diagram)