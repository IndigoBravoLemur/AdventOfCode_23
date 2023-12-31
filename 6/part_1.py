data = [line.split() for line in open('input.txt')]

data = [a[1:] for a in data]
print(data)
answer = 1
for race_number in range(len(data[0])):
    print(f"Race #{race_number}")
    race_length = int(data[0][race_number])
    record_distance = int(data[1][race_number])
    ways_of_winning = 0
    for i in range(race_length):
        length_travelled = i * (race_length-i) 
        if length_travelled > record_distance:
            ways_of_winning += 1
    print(f'Ways of beating record:{ways_of_winning}')
    answer = answer * ways_of_winning
print(answer)