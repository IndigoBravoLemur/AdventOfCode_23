#data = [line.strip('\n').split('\t') for line in open('input.txt')] # For some reason doesnt like splitting on tabs, specifically
data = [line.split() for line in open('input.txt')]

# 'del' is not an expression and cant be used directly in a list comprehension so an alternative needs to be used
#data = [del a[0] for a in data]
# This is effectively the same thing, returning a list with elements from position 1 onwards, ie, without [0]
data = [a[1:] for a in data]
print(data)

for race_number in range(len(data)):
    print(f"Race #{race_number}")
    race_length = data[0][race_number]
    record_distance = data[1][race_number]