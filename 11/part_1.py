g_map = [ line for line in open("test.txt")]

def expand_universe():
    # For each row in the universe map
    for i,row in enumerate(g_map):
        if "#" not in row:
            empty_rows.append(i)

def make_map():
    for row in g_map:
        for col in row:
            print(col, end="")
        print("")
    print()

empty_rows = []
expand_universe()
print(empty_rows)

# Once the list of empty rows has been identified, add rows into the array backwards so as not to throw off the indexing
for er in reversed(empty_rows):
    empty_row = ["."] * 13
    g_map.insert(er,empty_row)

make_map()
