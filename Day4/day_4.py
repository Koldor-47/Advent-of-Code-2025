# day Four of Advent of Code.

def read_map(file_path):
    paper_roll_map = []
    with open(file_path, "r") as AOC:
        for row in AOC:
            column = []
            row = row.strip()
            for col_num in row:
                column.append(col_num)
            paper_roll_map.append(column)

    return paper_roll_map

def find_moveable_rolls(the_diagram, part_b):
    moveable_rolls = 0
    current_x = 0
    current_y = 0
    max_cols = len(the_diagram[0])
    max_rows = len(the_diagram)
    map_size = (max_cols, max_rows)
    moveable_rolls_spots = []

    for index_x, row in enumerate(the_diagram):
        current_x = index_x
        for index_y, column in enumerate(row):
            current_y = index_y
            if the_diagram[current_x][current_y] == "@":
                num = search_neigbours(current_x, current_y, map_size, the_diagram)
                if num < 4:
                    moveable_rolls += 1
                    moveable_rolls_spots.append((current_x, current_y))
    
    #print(moveable_rolls, end="")
    #print(f" {moveable_rolls_spots}")
    #print("--" * 10)

    if not part_b:
        return moveable_rolls
    else:
        for loc in moveable_rolls_spots:
            the_diagram[loc[0]][loc[1]] = "."
    
        data = {
            "moveable_rolls" : moveable_rolls,
            "map" : the_diagram
        }
        return data

def search_neigbours(paper_roll_x, paper_roll_y, map_size, the_map):
    #print(f"current position X: {paper_roll_x} Y: {paper_roll_y} on a {map_size[0]}X{map_size[1]} grid")
    found_paper = -1

    if paper_roll_x == 0:
        start_row = 0
        end_row = 2
    elif paper_roll_x == map_size[0] - 1:
        start_row = -1
        end_row = 1
    else:
        start_row = -1
        end_row = 2

    if paper_roll_y == 0:
        start_col = 0
        end_col = 2
    elif paper_roll_y == map_size[1] - 1:
        start_col = -1
        end_col = 1
    else:
        start_col = -1
        end_col = 2

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            #print(f"{row} - {col}")
            #print(f"{the_map[paper_roll_x + row][paper_roll_y + col]}", end="")
            if the_map[paper_roll_x + row][paper_roll_y + col] == "@":
                found_paper += 1
        #print()
    
    return found_paper
            
        

if __name__ == "__main__":
    print("Day Four Advent of code....")
    TEST = r"Day4/test_puzzle_input.txt"
    REAL = r"Day4/puzzle_input.txt"

    theMap = read_map(REAL)

    a = find_moveable_rolls(theMap, False)

    rolls_moved = 0
    last_move = 1

    while last_move >= 1:
        data = find_moveable_rolls(theMap, True)
        last_move = data["moveable_rolls"]
        rolls_moved += last_move
        theMap = data["map"]
    
    print(rolls_moved)

###############
#
# get x,y location of paper-roll
# if posable search above, then above -1 and +1
# then if possalbe search +1 and -1
# the search below, then -1 and +1
# if count of paper around tested paper is greater 4 - can't get
#
