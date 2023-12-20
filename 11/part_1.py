g_map = [ [c for c in line.strip()] for line in open("test.txt")]

def expand_universe():
    # For each column in each row in the universe map
    for i in range(len(g_map)):
        is_empty = True
        for r in range(len(g_map)):
            if g_map[r][i] == "#":
                is_empty = False
        if is_empty:
            empty_cols.append(i)
    #print(empty_cols)

    # For the length of the row,check the column i for each row  
    # For each row in the universe map
    for i,row in enumerate(g_map):
        if "#" not in row:
            empty_rows.append(i)
    #print(empty_rows)

def make_map():
    sourceFile = open('demo.txt', 'w')
    for row in g_map:
        print(row, file = sourceFile)
        #print("",file = sourceFile)
    #print()
    sourceFile.close()

empty_rows = []
empty_cols = []
expand_universe()
#print(empty_rows)

# Once the list of empty rows has been identified, add rows into the array backwards so as not to throw off the indexing
for ec in reversed(empty_cols):
    empty_col = "."
    for r in g_map:
        r.insert(ec,empty_col)


# Once the list of empty rows has been identified, add rows into the array backwards so as not to throw off the indexing
for er in reversed(empty_rows):
    empty_row = ["."] * 13
    g_map.insert(er,empty_row)

galaxies = []
for r in range(len(g_map)):
    for ci, c in enumerate(g_map[r]):
        if c == "#":
            galaxies.append([r,ci])

diff_sum = 0
for gi, g in enumerate(galaxies):
    gr, gc = g
    #print(gr, gc)
    for gp in galaxies[gi:]:
        # Get shortest distance from the current to all galaxies beyond
        gpr, gpc = gp
        diff = abs(gpr-gr) + abs(gpc-gc)
        diff_sum += diff

print(diff_sum)
make_map()
#print(g_map)
#print("")
#print(galaxies)