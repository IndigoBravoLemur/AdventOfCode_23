import re
input_file = open("input.txt", "r")
lines = input_file.readlines()

id_total = 0
colour_dict = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
nump=0
numi=0
for game in lines:
    is_possible = True
    matched_string = re.search("^Game\s(\d+):(.*)", game)
    game_number = matched_string.group(1)
    sets_string = matched_string.group(2)
    set_list = sets_string.split(";")
    print(set_list)
    for set in set_list:
        pattern = re.compile(r'(\d+)\s(\w+)')
        for (number, colour) in re.findall(pattern, set):
            # If the number is greater than the possible number of cubes of that colour set possible as False
            if int(number) > colour_dict[colour]:
                print("game {} not possible as {} > {}".format(game_number, number, colour_dict[colour]))
                is_possible = False
                 
    if is_possible:
        id_total += int(game_number)
        nump+=1
        #print("adding {}".format(game_number))
    else:
        numi+=1

print(id_total)
print("total possible {} , total impossible {}".format(nump,numi))

