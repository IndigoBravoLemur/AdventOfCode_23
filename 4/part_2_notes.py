import re 

# Using list(match.groups()) returns a list of lists [['',''],['','']] whereas using match.groups() returns a list of tuples [('',''),('','')] - We need a list to add the multiplier field
# 'if match else None' is not required as we expect matches every line, but is good practice to use to filter out those lines which do not match the regex. 
### data2 = [list(match.groups()) if match else None for line in open('test.txt') if (match := re.search("Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)", line))]

# Return a tuple of the match groups for each line in the test file
pattern = "Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)"
# The match := is a walrus operator and allows the assignment of a variable inside a list comprehension
data = [list(match.groups())  for line in open('input.txt') if (match := re.search(pattern, line))]

# Appending an extra column to keep track of how many of each card you have
for index in data:
    index.append(1)

total_cards = 0
# enumerate returns each object in the list and also a iterator
for index,card in enumerate(data):
    # For as many cards, including duplicates awarded, find the winning numbers
    for multiplier in range(card[2]):
        winning_numbers = card[0].strip().split()
        my_numbers = card[1].strip().split()
        # For each number in my_numbers list, return that number if it is in the winning_numbers list
        matching_numbers = [number for number in my_numbers if number in winning_numbers]
        # Set range to (1,len(..)+1) so that it starts at 1, otherwise index 0 + iterator 0 = 0 and increments the wrong index
        for i in range(1,len(matching_numbers)+1):
            # Increment all proceeding indexes up to as many winning numbers awarded
            data[index+i][2]+=1
    print(f'Total matching numbers for {index+1} : {len(matching_numbers)}')      
    total_cards+=data[index][2] 

print(total_cards)