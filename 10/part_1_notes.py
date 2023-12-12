import sys
sys.setrecursionlimit(1000000)
# for each line in the file, seperate each character into an array and add the array to the map array
pipe_map = [[c for c in line.strip()] for line in open('input.txt')]

# get start position
for i,l in enumerate(pipe_map):
    if "S" in l:
        start_pos = (i, l.index("S"))
        print(f"start position:{start_pos}")

routing_dict = {        # Positional adjustments for valid neighbours (row,col)
    "|":((-1,0),(1,0)),  # Y-1, y+1
    "-":((0,-1),(0,1)),  # x-1, x+1
    "L":((-1,0),(0,1)),  # y-1, x+1
    "J":((-1,0),(0,-1)), # y-1, x-1
    "7":((1,0),(0,-1)),   # y+1, x-1
    "F":((1,0),(0,1))   # y-1, x+1
}
path = [start_pos]

def check_position(current_row, current_col):
    # unpack tuple of position coords
    
    parent_x, parent_y = path[-1]
    
    # Check pipe map if the new position is a pipe, starting position, or empty cell
    # Get character from pipe map
    c = pipe_map[current_row][current_col]

    if c == "S":
        print("Wonderful you found the end")
        return True
    elif c == ".":
        return False
    else:
        # Charactger is pipe
        # Getting routing dict modifiers so its more readable than accessing it directly
        route1_row, route1_col = routing_dict[c][0]
        route2_row, route2_col = routing_dict[c][1]

        newr1 = route1_row + current_row
        newc1 = route1_col + current_col
        newr2 = route2_row + current_row
        newc2 = route2_col + current_col

        # If parent node coords match those of one of the two possible connecting coords of  this node then move to the other coord
        if (newr1, newc1) == (parent_x,parent_y):
            # If coords match the parent then its a valiud route to the current node, add the current position to the path
            path.append([current_row,current_col])
            #print(len(path))
            return check_position(newr2, newc2)
        elif (newr2, newc2) == (parent_x,parent_y):
            path.append([current_row,current_col])
            #print(len(path))
            return check_position(newr1, newc1)
        else:
            # None of the two possible coords match the originating node therefore its a bad route
            return False

# Check the currounding coords around the S position and check position for each one, which will start a recursive call until it finds S or fails to find a valid adjacent position
s_routing = ((0,1),(-1,0),(0,-1),(1,0))
route_complete = False
for i, route in enumerate(s_routing):
    print(f"i is {i}")
    print(route_complete)
    if not route_complete:
        # If the S char as not been found, and the route completed check the next adjacent position to the start point
        new_row = s_routing[i][0]+start_pos[0]
        new_col = s_routing[i][1]+start_pos[1]
        route_complete = check_position(new_row,new_col)

print("hello")
steps = len(path)/2
print(steps)