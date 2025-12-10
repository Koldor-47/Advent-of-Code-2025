# Advent of Code Day 6
import math

from itertools import zip_longest

def read_homework(file_path):
    numbers = []
    math_lines = 3
    instructions_line = -1 # last line
    instructions = []

    with open(file_path, "r") as AOC:
        data = []
        for line in AOC:
            line = line[:-1]
            data.append(line)
        numbers = data[:math_lines]
        instructions = data[-1]
        instructions = instructions.strip().split()

    maths_workbook = {
        "numbers" : numbers,
        "instructions" : instructions
    }

    return maths_workbook
 
def str_to_int(math_numbers):
    all_rows = []
    for row in math_numbers:
        numbers = row.split()
        numbers = list(map(int, numbers))
        all_rows.append(numbers)

    return all_rows

    #for str_list in txt_numbers:
    #    numbers = list(map(int, str_list))
    #    real_number.append(numbers)

   # return numbers

def check_maths(maths_book, number_questions):
    total = []
    for problem_num in range(0, number_questions):
        problem_numbers = [maths_book["real_numbers"][0][problem_num], maths_book["real_numbers"][1][problem_num], maths_book["real_numbers"][2][problem_num]]
        if maths_book["instructions"][problem_num] == "*":
            answer = math.prod(problem_numbers)
        elif maths_book["instructions"][problem_num] == "+":
            answer = sum(problem_numbers)
        
        
        print(f"{maths_book["real_numbers"][0][problem_num]} {maths_book["instructions"][problem_num]} {maths_book["real_numbers"][1][problem_num]} {maths_book["instructions"][problem_num]} {maths_book["real_numbers"][2][problem_num]} = {answer}")
        total.append(answer)
    
    return sum(total)


def check_math_partB(math_book, number_questions):
    total = []
    numbers = {
        "first" : [],
        "second" : [],
        "last" : []
    }
    for row, nums in zip(math_book["numbers"], numbers.keys()):
        numbers[nums] = row

    for the_first, the_second, the_third in zip(numbers["first"], numbers["second"], numbers["last"]):
        new_num = [the_first, the_second, the_third]
        the_new_number = []
        for num in new_num:
            if num:
                the_new_number.append(num)
        
        print("".join(the_new_number))
        
if __name__ == "__main__":
    print("day 6 Advent of Code")

    TEST = r"Day6/test_input.txt"
    REAL = r"Day6/puzzle_input.txt"

    maths_book = read_homework(TEST)

    maths_book["real_numbers"] = str_to_int(maths_book["numbers"])

    #part_a = check_maths(maths_book, 4)
    part_b = check_math_partB(maths_book, 4)
    print(part_b)


# too Low 19745445035

