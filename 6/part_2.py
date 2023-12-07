#data = [line.strip('\n').split('\t') for line in open('input.txt')] # For some reason doesnt like splitting on tabs, specifically
data = [line.split() for line in open('input.txt')]

# 'del' is not an expression and cant be used directly in a list comprehension so an alternative needs to be used
#data = [del a[0] for a in data]
# This is effectively the same thing, returning a list with elements from position 1 onwards, ie, without [0]
data = [a[1:] for a in data]
data[0] = "".join(data[0])
data[1] = "".join(data[1])
print(data)
answer = 1

for race_number in range(len(data)):
    print(f"Race #{race_number}")
    race_length = int(data[0])
    record_distance = int(data[1])
    print(f'length - {race_length} distance - {record_distance}')
    ways_of_winning = 0
    for i in range(race_length): # Each i is time held down
        # Length travelled = Speed * (Race Length - time held button down)
        length_travelled = i * (race_length-i) 
        if length_travelled > record_distance:
            ways_of_winning += 1
    print(f'Ways of beating record:{ways_of_winning}')
    answer = answer * ways_of_winning
print(answer)
