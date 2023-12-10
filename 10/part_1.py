# for each line in the file, seperate each character into an array and add the array to the map array
pipe_map = [[c for c in line.strip()] for line in open('test.txt')]

# get start position
for i,l in enumerate(pipe_map):
    if "S" in l:
        start_pos = (i, l.index("S"))
        print(f"start position:{start_pos}")

routing_dict = {        # Positional adjustments for valid neighbours
    "|":((0,-1),(0,1)),  # Y-1, y+1
    "-":((-1,0),(1,0)),  # x-1, x+1
    "L":((0,-1),(1,0)),  # y-1, x+1
    "J":((0,-1),(-1,0)), # y-1, x-1
    "7":((0,1),(-1,0)),   # y+1, x-1
    "F":((0,-1),(1,0))   # y-1, x+1
}
routes = routing_dict["|"][0]
print(routes)

current_route = []
# Need to append new valid positions to the array and then pop them off if its a dead end
current_route.append([3,4])

def check_position(position):
    # unpack tuple of position coords
    (x, y) = position
    # take last position in the array, the parent node
    px, py = current_route[-1]
    print(px, py)
    # check pipe map if
    c = pipe_map[x][y]
    oo = routing_dict[c][0][0]
    print(oo)
    #rx, ry = routing_dict[c][0]
    if routing_dict[c][0][0]+x==px and routing_dict[c][0][1]+y == py:
        # if coords match the parent then use the other coord set
        position
        new_position = (routing_dict[c][1][1]+x, routing_dict[c][1][1]+y)
        check_position(new_position)

    #check previous position coord, if whichever it matches follow the other coord.ConnectionRefusedError
testpos = (1,3)
check_position(testpos)
#check_position(start_pos)    
# Take position
# read character
# check if corresponding position is valid (is one of two possible coords)

# checkposition -
#       for each position check if it is valid
#       for each valid coord 
#               if its not S
#                   run checkposition on given cord
#               if it is S
#                     return True, route complete 
#       return
#
#
