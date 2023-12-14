g_map = [ line.strip() for line in open("test.txt")]

def expand_universe():
    # For each row in the universe map
    for i,row in enumerate(g_map):
        if "#" not in row:
            empty_rows.append(i)

def make_map1():
    for row in g_map:
        print(row)
        #for col in row:
            #print(col, end="")
        #print("")
    #print()

def make_map():
    sourceFile = open('demo.txt', 'w')
    for row in g_map:
        print(row, file = sourceFile)
        #print("",file = sourceFile)
    #print()
    sourceFile.close()

empty_rows = []
expand_universe()
#print(empty_rows)

# Once the list of empty rows has been identified, add rows into the array backwards so as not to throw off the indexing
for er in reversed(empty_rows):
    empty_row = "............."
    print(er)
    g_map.insert(er,empty_row)

make_map()
print(g_map)