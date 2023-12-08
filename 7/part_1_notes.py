hands = [line.split() for line in open('test2.txt')]

from collections import Counter
from operator import itemgetter

def most_frequent_character(hand):
    char_count = Counter(hand)
    print(char_count)
    # Returns the largest item in an iterable - The key argument specifies a one-argument ordering function like that used for list.sort() 
    # The .get method is a method of the Counter dictionary type.
    ## In the context of dictionaries, the .get method takes a single argument (the key) and returns the corresponding value. 
    ## However, when used as a key function for max, the max function implicitly calls .get on each key without passing any additional arguments.
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
    print(f"The most frequent character in '{hand}' is: {result} {strength}")

# https://stackoverflow.com/questions/64576903/how-to-sort-the-list-in-custom-order-in-python
# Create a dictionary of cards to values to use for sorting
card_weighting = {card:iterator for iterator,card in enumerate(['1','2','3','4','5','6','7','8','9','T','J','Q','K','A'])}
#hands.sort(key=lambda card: (float(card[2]), card_weighting.get(card[0])))

## split number into subarray?
# Sort the list based on the second index in each sublist, ie the strength.
# In case of a tie, which will occur on all instances of the same card type, it sorts based on the second condition, the custom sorting function
# Not working. Sorting the strength but not the card weighting
# The key parameter expects a function that takes an element from the iterable (in this case, a sublist) and returns a value that will be used as the sorting key.
#hands.sort(key=lambda card: (float(card[2])))
#for h in hands:
#    print(h)

# Can use itemgettr instead of anonymous function (buyt requires import)
hands.sort(key=itemgetter(2), reverse=True)
for h in hands:
    print(h)

#hands.sort(key=lambda card: ())
#for h in hands:
#    print(h)

#hands.sort(key=lambda card: (card_weighting.get(card[0][0])))

#for h in hands:
#    print(h)