# day Five AOC 2025

def read_ingredient_db(file_path):
    fresh_ranges = []
    ingredients = []
    with open(file_path, "r") as AOC:
        blank_line = False
        for line in AOC:
            if line == "\n":
                blank_line = True
            elif not blank_line:
                start, end = line.strip().split("-")
                start = int(start)
                end = int(end)
                fresh_ranges.append((start, end))
            else:
                ingredient = line.strip()
                ingredient = int(ingredient)
                ingredients.append(ingredient)

    
    data = {
        "fresh_ranges" : fresh_ranges,
        "ingredients" : ingredients
    }

    return data

def make_fresh(fresh_ranges):
    new_fresh_ranges = []
    print("Making Ranges....")
    low = None
    high = 0
    sorted_ranges = sorted(fresh_ranges)
    for index, r in enumerate(sorted_ranges):
        if index + 1 < len(sorted_ranges):
            next_item = index + 1
            current_high = r[1]
            current_low = r[0]
            next_high = sorted_ranges[next_item][1]
            next_low= sorted_ranges[next_item][0]
            if next_low <= current_high and next_low >= current_low:
                #print(f"{r} - {sorted_ranges[next_item]}")
                if low is None:
                    low = current_low
                elif low > current_low:
                    low = current_low
                if high < next_high:
                    high = next_high
            elif low is not None and high is not None:
                new_fresh_ranges.append(range(low, high+1))
                low = None
                high = 0
            else:
                new_fresh_ranges.append(range(r[0], r[1]+1))

        if index + 1 == len(sorted_ranges):
            if low is not None:
                new_fresh_ranges.append(range(low, high+1))
            elif low is None:
                new_fresh_ranges.append(range(r[0], r[1]+1))


    
    return new_fresh_ranges


def make_fresh_two(fresh_ranges):
    big_range = []
    for fresh_range in fresh_ranges:
        big_range.append(range(fresh_range[0], (fresh_range[1] + 1)))
    
    return big_range
        




if __name__ == "__main__":
    print("Solving Day 5 AOC 2025")
    TEST = r"day5/test_input.txt"
    REAL = r"day5/puzzle_input.txt"

    data = read_ingredient_db(REAL)

    the_fresh_ranges = make_fresh_two(data["fresh_ranges"])
    ingredients = sorted(data["ingredients"], reverse=True)
    fresh = []
    count = 0
    print(f"there are {len(ingredients)} ingredients and there are fresh ids {len(the_fresh_ranges)}")
    
    while count < len(the_fresh_ranges):
        ingredients_left = len(ingredients)
        while ingredients_left >= 0:
            if ingredients[ingredients_left-1] in the_fresh_ranges[count]:
                fresh.append(ingredients[ingredients_left-1])
                ingredients.pop(ingredients_left-1)
            
            ingredients_left -= 1
                
                    

        count += 1
    
    print(f"There are {len(fresh)} fresh ingrendients")

    print(f"the current length of the ingredients is {len(ingredients)}")

    print(len(set(fresh)))


# Answer 782

# too Low 752 hmmmm
# too low 753 hmmm

# not right 781 < used_fresh_two
# not Right 955 <- used make_fresh_two
# upper is 1000 

