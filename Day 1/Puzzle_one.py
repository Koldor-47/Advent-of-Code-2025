# Day one Advent of code

def read_file(file_path):
    data = []
    with open(file_path, 'r') as AOC:
        for line in AOC:
            data.append(line.strip())
    
    return data

def get_moveby(current_number, moveby, direction):

    if direction.lower() == "l":
        current_number = current_number - moveby
    elif direction.lower() == 'r':
        current_number = current_number + moveby
    
    if current_number > 99:
        current_number = (current_number % 100)
        return current_number
    elif current_number < 0:
        current_number = (current_number % 100)
        return current_number
    else:
        return current_number

def main():
    rotation_instructions = read_file(r"Day 1\puzzle_input.txt")
    starting_point = 50
    max_point = 99
    zero_count = 0
    combo = starting_point

    for combo_num in rotation_instructions:
        direction = combo_num[0]
        moveby = combo_num[1:]
        moveby = int(moveby)

        combo = get_moveby(combo, moveby, direction)
        if combo == 0:
            zero_count += 1

    print(zero_count)

if __name__ == "__main__":

    main()
