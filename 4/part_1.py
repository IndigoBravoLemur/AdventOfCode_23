import re 
data = [re.search("Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)", line) for line in open('input.txt')]
point_total = 0
for card in data:
    card_points = 0
    winning_numbers = re.split(r'\s+', card.group(1).strip())
    my_numbers = re.split(r'\s+', card.group(2).strip())
    matching_numbers = [number for number in my_numbers if number in winning_numbers]
    if len(matching_numbers) >= 1:
        card_points = pow(2,len(matching_numbers)-1)
    point_total += card_points

print(point_total)