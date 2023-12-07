import re 

# Using list(match.groups()) returns a list of lists [['',''],['','']] whereas using match.groups() returns a list of tuples [('',''),('','')] - We need a list to add the multiplier field
# 'if match else None' is not required as we expect matches every line, but is good practice to use to filter out those lines which do not match the regex. 
### data2 = [list(match.groups()) if match else None for line in open('test.txt') if (match := re.search("Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)", line))]

# Return a tuple of the match groups for each line in the test file
pattern = "Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)"
data = [list(match.groups())  for line in open('input.txt') if (match := re.search(pattern, line))]

for index in data:
    index.append(1)

total_cards = 0
for index,card in enumerate(data):
    for multiplier in range(card[2]):
        winning_numbers = card[0].strip().split()
        my_numbers = card[1].strip().split()
        matching_numbers = [number for number in my_numbers if number in winning_numbers]
        # Set range to (1,len(..)+1) so that it starts at 1, otherwise index 0 + iterator 0 = 0 and increments the wrong index
        for i in range(1,len(matching_numbers)+1):
            data[index+i][2]+=1
    print(f'Total matching numbers for {index+1} : {len(matching_numbers)}')      
    total_cards+=data[index][2] 

print(total_cards)