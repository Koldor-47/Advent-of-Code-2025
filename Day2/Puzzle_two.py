# Day 2 AOC 

def read_puzzle_data(file_path):
    with open(file_path, 'r') as AOC:
        data = AOC.readline()
        data = data.strip().split(",")

        return data

def puzzle(puzzle_data):
    invalid_ids = []

    for id in puzzle_data:
        low, high = id.split("-")

        if len(low) % 2 == 0:
            number_length = len(low) / 2
            number_first = low[:int(number_length)]
            in_Range = True
            while in_Range:
                silly_pattern = int(number_first+number_first)
                if silly_pattern <= int(high) and silly_pattern >= int(low):
                    invalid_ids.append(int(silly_pattern))
                elif silly_pattern > int(high):
                    in_Range = False
                
                number_first = str(int(number_first) + 1)
        elif len(high) % 2 == 0:
            number_length = len(high) / 2
            number_first = high[:int(number_length)]
            in_Range = True
            while in_Range:
                silly_pattern = int(number_first+number_first)
                if silly_pattern >= int(low) and silly_pattern <= int(high):
                    invalid_ids.append(int(silly_pattern))
                elif silly_pattern < int(low):
                    in_Range = False
                
                number_first = str(int(number_first) - 1)
        else:
            print(f"{low} = {high}")
    
    return invalid_ids

        

if __name__ == "__main__":
    print("Day 2 Advent Of Code 2025")

    test_input = r"Day2\puzzle_input.txt"

    puzzle_data = read_puzzle_data(test_input)

    answer = puzzle(puzzle_data)

    print(sum(answer))

    # too Low 11277648113,
    #         16793817782 
    #          1227775554