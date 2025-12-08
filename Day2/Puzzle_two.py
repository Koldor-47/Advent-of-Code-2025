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

def puzzle_b(first_id, last_id):
    invalid_ids = []

    first_num = int(first_id)
    last_num = int(last_id)

    if len(last_id) > len(first_id):
        invalid_ids = number_change(first_id, last_id)
    else:
        # i think i need recusion hmmmm
        invalid_ids = get_invalid_ids(first_id, last_id, len(first_id))

    return invalid_ids

def get_invalid_ids(first_id, last_id, id_length):
    invalid_ids = []
    patterns = []
    keep_going = True
    test_length = id_length
    while keep_going:    
        if id_length // test_length == id_length / test_length:
            pattern_len = int(id_length / test_length)
            pattern = first_id[:pattern_len]
            below_lastid = True
            while below_lastid:
                num = int(pattern * test_length)
                if num <= int(last_id):
                    if num <= int(last_id) and num >= int(first_id) and len(str(num)) > 1:
                        invalid_ids.append(num)
                else:
                    below_lastid = False
                
                up = int(pattern) + 1
                pattern = str(up)
            

        test_length -= 1
        if test_length <= 1: 
            #print("breaking")
            break
    
    print(invalid_ids)
    return invalid_ids


def number_change(first_id, last_id):
    invalid_ids = []
    upper_first = len(first_id) * "9"
    num_upper = int(upper_first)
    lower_last = str(num_upper + 1)

    lower = get_invalid_ids(first_id, upper_first, len(first_id))
    upper = get_invalid_ids(lower_last, last_id, len(lower_last))

    invalid_ids.extend(lower)
    invalid_ids.extend(upper)

    return invalid_ids


def go_though_ids(puzzle_data):
    invalid_ids = []
    for id in puzzle_data:
        first, last = id.split("-")
        bad_ids = puzzle_b(first, last)
        invalid_ids.extend(bad_ids)
    
    return list(set(invalid_ids))
    
        

if __name__ == "__main__":
    print("Day 2 Advent Of Code 2025")

    test_input = r"day3/test_input.txt"
    puzzle_data = read_puzzle_data(test_input)
    answer = go_though_ids(puzzle_data)

    print(sum(answer))

    # part b too low
    # 21966241186
    # 27469417393


    # too Low 11277648113,
    #         16793817782 
    #          1227775554