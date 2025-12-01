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
    
def get_moveby_partb(starting_pointer, amount_moved, direction):
    past_zero = 0
    real_position = 0
    move_difference = amount_moved

    
    if amount_moved >= 100:
        past_zero = amount_moved // 100
        move_difference = amount_moved % 100

    if direction.lower() == "l":
        current_position = starting_pointer - move_difference
    elif direction.lower() == 'r':
        current_position = starting_pointer + move_difference


    if current_position == 0:
        past_zero += 1
    elif current_position <= 99 and current_position > 0:
        real_position = current_position
    elif current_position > 99 or current_position < 0:
        if starting_pointer != 0:
            past_zero += 1
        real_position = current_position % 100
    
    
     


    


    return (real_position, past_zero)

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

        combo = get_moveby_partb(combo, moveby, direction)

        if combo[1] > 0:
            zero_count += combo[1]
        
        combo = combo[0]

    print(zero_count)

if __name__ == "__main__":

    
    t1 = get_moveby_partb(98, 1, "R")
    t2 = get_moveby_partb(1, 2, "L")
    t3 = get_moveby_partb(12, 300, "R")
    t4 = get_moveby_partb(12, 312, "L")

    print(t1)
    print(t2)
    print(t3)
    print(t4)


    main()