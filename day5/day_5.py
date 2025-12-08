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
    print("Making Ranges....")
    fresh_ingredients = {}

    for the_range in fresh_ranges:
        for item in range(the_range[0], the_range[1] + 1):
            if item not in fresh_ingredients:
                fresh_ingredients[item] = "Fresh"
    
    return fresh_ingredients


if __name__ == "__main__":
    print("Solving Day 5 AOC 2025")
    TEST = r"day5/test_input.txt"
    REAL = r"day5/puzzle_input.txt"

    data = read_ingredient_db(TEST)

    the_fresh_ingredients = make_fresh(data["fresh_ranges"])
