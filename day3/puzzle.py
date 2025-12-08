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

def part_b(data):
    jolts = [0]

    for line in data:
        jolt = get_bigger_jolt(line)
        jolts.append(jolt)
    
    return sum(jolts)
    
    
    
def get_bigger_jolt(bank):
    battery_bank_length = len(bank)
    battery_size = 12
    starting_from = 0
    hightest_num = 0
    biggest_jolt = []

    while battery_size > 0:
        
        for index, battery in enumerate(bank):
            battery_bank_length = len(bank)
            spaces_left = (battery_bank_length) - index
            battery = int(battery)

            if spaces_left < battery_size:
                break
            if hightest_num < battery and spaces_left >= battery_size :
                hightest_num = battery
                last_found_index = index

        biggest_jolt.append(str(hightest_num))
        hightest_num = 0
        battery_size -= 1
        starting_from = last_found_index +1
        #print(f"full list {bank}")
        
        
        bank = bank[starting_from:]
        
        #print(f"{bank[starting_from:]}")
    
    return int("".join(biggest_jolt))
    

    
    
    

if __name__ == "__main__":
    print("day 3")
    test_path = Path(r"day3/puzzle_input.txt")

    battery_banks = read_input(test_path)

    print(part_b(battery_banks))


# too low
# 141933376811866'
# 
# 
#  the Answer
# 169709990062889