# Advent of Code Day 6

def read_homework(file_path):
    numbers = []
    math_lines = 3
    instructions_line = -1 # last line
    instructions = []

    with open(file_path, "r") as AOC:
        data = []
        for line in AOC:
            line = line.strip()
            data.append(line)
        numbers = data[:math_lines]
        instructions = data[instructions_line]
    
    maths_workbook = {
        "numbers" : numbers,
        "instructions" : instructions

    }

    return maths_workbook
 

if __name__ == "__main__":
    print("day 6 Advent of Code")

    TEST = r"Day6/test_input.txt"
    REAL = r"Day6/puzzle_input.txt"

    maths_book = read_homework(REAL)

    print(maths_book["numbers"][0].split())