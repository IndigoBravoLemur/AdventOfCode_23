import re 

pattern = "Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)"
data = [list(match.groups()) for line in open('input.txt') if (match := re.search(pattern, line))]

for index in data:
    index.append(1)

total_cards = 0
for index,card in enumerate(data):
    for multiplier in range(card[2]):
        winning_numbers = card[0].strip().split()
        my_numbers = card[1].strip().split()
        matching_numbers = [number for number in my_numbers if number in winning_numbers]
        for i in range(1,len(matching_numbers)+1):
            data[index+i][2]+=1
    total_cards+=data[index][2] 

print(total_cards)