from collections import Counter
from operator import itemgetter
hands = [line.split() for line in open('input.txt')]

def most_frequent_character(hand):
    char_count = Counter(hand)
    most_frequent = max(char_count, key=char_count.get)
    frequency = char_count[most_frequent]
    if frequency == 3 or frequency == 2:
        char_count.pop(most_frequent)
        second_most_frequent = max(char_count, key=char_count.get)
        second_frequency = char_count[second_most_frequent]
        if second_frequency == 2:
            frequency = frequency+(second_frequency/10)
    return most_frequent, frequency

for hand in hands:
    result, strength = most_frequent_character(hand[0])
    hand.append(strength)

card_weighting = {card:iterator for iterator,card in enumerate(['2','3','4','5','6','7','8','9','T','J','Q','K','A'])}

for i in range(4, -1, -1):
    hands.sort(key=lambda card: (card_weighting.get(card[0][i])))

hands.sort(key=itemgetter(2))
total_winnings = 0
for i,h in enumerate(hands):
    hand_winnings = int(h[1])*(i+1)
    total_winnings += hand_winnings

print(total_winnings)
