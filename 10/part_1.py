import sys
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