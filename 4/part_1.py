import re 
data = [re.search("Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)", line) for line in open('test.txt')]
print(data[0].group(2))
point_total = 0
for card in data:
    card_points = 0
    winning_numbers = re.split(r'\s+', card.group(1).lstrip())
    my_numbers = re.split(r'\s+', card.group(2).lstrip())
    print(my_numbers)
    print(winning_numbers)
    matching_numbers = [number for number in my_numbers if number in winning_numbers]
    print(matching_numbers)
    print(len(matching_numbers))
    if len(matching_numbers) >= 1:
        card_points = pow(card_points+1,len(matching_numbers)-1)
    
    point_total += card_points

print(point_total)