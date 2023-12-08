from collections import Counter
from operator import itemgetter

hands = [line.split() for line in open('input.txt')]

def most_frequent_character(hand):
    j_frequency = 0
    char_count = Counter(hand)
    if 'J' in char_count:
        j_frequency = char_count['J']
        char_count.pop('J')
        if j_frequency == 5:
            return j_frequency
    
    most_frequent = max(char_count, key=char_count.get)
    frequency = char_count[most_frequent]
    frequency += j_frequency
    if frequency == 3 or frequency == 2:
        char_count.pop(most_frequent)
        second_most_frequent = max(char_count, key=char_count.get)
        second_frequency = char_count[second_most_frequent]
        if second_frequency == 2:
            frequency = frequency+(second_frequency/10)
    return frequency

for hand in hands:
    strength = most_frequent_character(hand[0])
    hand.append(strength)

card_weighting = {card:iterator for iterator,card in enumerate(['J','2','3','4','5','6','7','8','9','T','Q','K','A'])}

for i in range(4, -1, -1):
    hands.sort(key=lambda card: (card_weighting.get(card[0][i])))

hands.sort(key=itemgetter(2))
total_winnings = 0
for i,h in enumerate(hands):
    hand_winnings = int(h[1])*(i+1)
    total_winnings += hand_winnings

print(total_winnings)
