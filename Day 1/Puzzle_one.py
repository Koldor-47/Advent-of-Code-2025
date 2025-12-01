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
    
def get_moveby_partb(current_number, moveby, direction):

    past_zero = 0

    if direction.lower() == "l":
        current_number = current_number - moveby
    elif direction.lower() == 'r':
        current_number = current_number + moveby
    

    if current_number > 99 and current_number <= 100:
        current_number = (current_number % 100)
        past_zero += 1
    elif current_number > 100:
        past_zero = current_number // 100
        current_number = (current_number % 100)

    elif current_number <= 0 and current_number >= -100:
        current_number = (current_number % 100)
        past_zero += 1
    elif current_number < -99:
        past_zero = abs(current_number // 100)
        current_number = (current_number % 100)
        

    return (current_number, past_zero)

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

    
    t1 = get_moveby_partb(10, 15, "L")
    t2 = get_moveby_partb(10, 200, "L")
    t3 = get_moveby_partb(50, 50, "R")
    t4 = get_moveby_partb(50, 150, "R")
    t5 = get_moveby_partb(50, 1000, "R")
    t6 = get_moveby_partb(50, 1000, 'L')
    t7 = get_moveby_partb(0, 1, "L")
    t8 = get_moveby_partb(0, 300, "R")
    t10 = get_moveby_partb(45, 958, "R")
    t11 = get_moveby_partb(98, 103, "L")
    t12 = get_moveby_partb(95, 5, "R")
    t13 = get_moveby_partb(5, 105, "L")
    t14 = get_moveby_partb(5, 60, "L")

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
    print(t6)
    print(t7)
    print(t8)
    print(t10)
    print(t11)
    print(t12)
    print(t13)
    print(t14)

    main()
    