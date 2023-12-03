import re
input_file = open("input.txt", "r")
lines = input_file.readlines()
total_power = 0

for game in lines:
    max_game_colours = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }
    matched_string = re.search("^Game\s(\d+):(.*)", game)
    game_number = matched_string.group(1)
    sets_string = matched_string.group(2)
    set_list = sets_string.split(";")
    for set in set_list:
        pattern = re.compile(r'(\d+)\s(\w+)')
        for (number, colour) in re.findall(pattern, set):
            # If the number is greater than current max of that colour in this game 
            if int(number) > max_game_colours[colour]:
                max_game_colours[colour] = int(number)
    game_power = max_game_colours["red"]*max_game_colours["green"]*max_game_colours["blue"]
    print("Game power for {} is {}".format(game_number,game_power))           
    total_power += game_power

print(total_power)
