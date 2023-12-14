import sys
from itertools import zip_longest

sys.setrecursionlimit(1000000)
pipe_map = [[c for c in line.strip()] for line in open('input.txt')]

for i,l in enumerate(pipe_map):
    if "S" in l:
        start_pos = (i, l.index("S"))
        print(f"start position:{start_pos}")

routing_dict = {        
    "|":((-1,0),(1,0)), 
    "-":((0,-1),(0,1)),  
    "L":((-1,0),(0,1)), 
    "J":((-1,0),(0,-1)), 
    "7":((1,0),(0,-1)),   
    "F":((1,0),(0,1))   
}
path = [start_pos]

def check_position(current_row, current_col):    
    parent_x, parent_y = path[-1]
    c = pipe_map[current_row][current_col]
    if c == "S":
        print("End of loop found")
        return True
    elif c == ".":
        return False
    else:
        route1_row, route1_col = routing_dict[c][0]
        route2_row, route2_col = routing_dict[c][1]

        newr1 = route1_row + current_row
        newc1 = route1_col + current_col
        newr2 = route2_row + current_row
        newc2 = route2_col + current_col

        if (newr1, newc1) == (parent_x,parent_y):
            path.append([current_row,current_col])
            return check_position(newr2, newc2)
        elif (newr2, newc2) == (parent_x,parent_y):
            path.append([current_row,current_col])
            return check_position(newr1, newc1)
        else:
            return False

s_routing = ((0,1),(-1,0),(0,-1),(1,0))
route_complete = False
for i, route in enumerate(s_routing):
    if not route_complete:
        new_row = s_routing[i][0]+start_pos[0]
        new_col = s_routing[i][1]+start_pos[1]
        route_complete = check_position(new_row,new_col)

steps = len(path)/2
print(steps)
print("--------")
print()

# part 2
pipe_map[start_pos[0]][start_pos[1]] = "7"

def make_map():
    sourceFile = open('demo.txt', 'w')
    for col in pipe_map:
        for char in col:
            print(char, end="", file = sourceFile)
        print("",file = sourceFile)
    print()
    sourceFile.close()

# Build the rows which you can squeeze though by comparing characters on adjacent rows
def build_squeezeable_rows():
    # Go through the pipe map row by row and check the current and next row for areas to squeeze through, excluding the last element in the array [:-1]
    # Imagine the first of the pair is on the top row and second on the bottom row
    valid_row_pairs = (("|","|"),("7","|"),("F","|"),("7","L"),("7","J"),("|","L"),("|","J"),("F","L"),("F","J"))
    row_index = 0 
    while row_index < len(pipe_map[:-1]):
        new_row = []
        current_row = pipe_map[row_index]
        next_row = pipe_map[row_index+1]
        for (cr_char, nr_char) in (zip(current_row, next_row)):
            if (cr_char, nr_char) in valid_row_pairs:
                # If valid pair is found, add a "." as it can be squeezed through
                new_row.append("|")
            elif (cr_char, nr_char) == (".","."):
                # If both chars are "." then add a "." to indicate an empty space
                new_row.append(".")
            else:
                new_row.append(".")
        pipe_map.insert(row_index+1,new_row)
        row_index += 2

# Build the cols which you can squeeze though by comparing characters on adjacent cols
def build_squeezeable_cols():
    # Go through the pipe map column by column and check the current and next column for areas to squeeze through, excluding the last element in the array
    # Imagine the first of the pair is on the left and second on the right
    valid_col_pairs = (("-","-"),("L","-"),("F","-"),("-","J"),("-","7"),("L","J"),("L","7"),("F","J"),("F","7"))
    # While row index is less than pipe map length
    # for each row check the 0,1 indexes of chars etc etc and add element
    for row_index,row in enumerate(pipe_map):
        new_col_data=[]
        for col_index in range(len(row)-1):
            current_col = row[col_index]
            next_col = row[col_index+1]
            if (current_col, next_col) in valid_col_pairs:
                new_col_data.append("-")
            elif (current_col, next_col) == (".","."):
                # If both chars are "." then add a "." to indicate an empty space
                new_col_data.append(".")
            else:
                new_col_data.append(".")
        #print("orinting")
        #print(row)
        #print(new_col_data)       
        # For the given row, add in the new column data by creating a new row, which is the product of zipping the new row data and the old row together
        ## i.e for each pair ("-","|") created by zipping the row and new column data, iterate over that pair (for item in pair) and return that item
        pipe_map[row_index]=[item for pair in zip(row, new_col_data) for item in pair]
        # Because the zipped lists are not of equal length and the order in which they are taken, one is left out at the end so im doing this
        pipe_map[row_index].append(row[-1])
#make_map()
# for each row, add element in the index of the current col
build_squeezeable_rows()
#make_map()
build_squeezeable_cols()
#make_map()

print("")

nr = 53
nc = 99

def flood_fill(row, col):
    if 0 <= row < len(pipe_map) and 0 <= col < len(pipe_map[0]) and pipe_map[row][col] == ".":
        # Mark the current cell
        pipe_map[row][col] = "*"

        # Check and fill neighbors
        flood_fill(row - 1, col)  # above
        flood_fill(row + 1, col)  # below
        flood_fill(row, col - 1)  # left
        flood_fill(row, col + 1)  # right

flood_fill(nr,nc)
make_map()

# now, remove every other row.
pipe_map = pipe_map[::2]
for i,r in enumerate(pipe_map):
    pipe_map[i]=r[::2]

count = 0 
for v in pipe_map:
    for b in v:
        if b == "*":
            count += 1

#make_map()
print(count)