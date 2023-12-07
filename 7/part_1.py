# list of hands, 5 cards each - AKQJT 9-2 A high
#       [['1','2','3','4','5'],['1','2','3','4','5']]
# Hands have ONE type
# order based on strength
# reduce ? - no , applies a function to eachelement in list and reduces to a singe output ? 
#can get strength of hand by reducing on the list  is that fast
hands = [line.split() for line in open('test.txt')]

# An array of each type containing tuples of hand and bet size ?
five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []

from collections import Counter

def most_frequent_character(hand):
    char_count = Counter(hand)
    print(char_count)
    # Returns the largest item in an iterable - The key argument specifies a one-argument ordering function like that used for list.sort() 
    # The .get method is a method of the Counter dictionary type.
    ## In the context of dictionaries, the .get method takes a single argument (the key) and returns the corresponding value. 
    ## However, when used as a key function for max, the max function implicitly calls .get on each key without passing any additional arguments.
    most_frequent = max(char_count, key=char_count.get)
    frequency = char_count[most_frequent]
    if frequency == 3:
        print("")
        
    return most_frequent, frequency

for hand in hands:
    result, frequency = most_frequent_character(hand[0])
    hand.append(frequency)
    print(f"The most frequent character in '{hand}' is: {result} {frequency}")
