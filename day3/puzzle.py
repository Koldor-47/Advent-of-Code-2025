# Day 3 Puzzle
from pathlib import Path

def read_input(file_path):
    data = []
    with open(file_path, 'r') as AOC:
        for row in AOC:
            data.append(row.strip())
    
    return data

def part_a(data):
    jolts = []

    for line in data:
        jolt = get_jolt_rating(line)
        jolts.append(jolt)

    print(sum(jolts))

def get_jolt_rating(bank):
    first_max = max(bank[:-1])
    first_index = bank.index(first_max)
    second_max = max(bank[first_index+1:])

    jolt_num = first_max + second_max
    return int(jolt_num)


if __name__ == "__main__":
    print("day 3")
    test_path = Path(r"day3/puzzle_input.txt")

    battery_banks = read_input(test_path)

    part_a(battery_banks)