# list of hands, 5 cards each - AKQJT 9-2 A high
#       [['1','2','3','4','5'],['1','2','3','4','5']]
# Hands have ONE type
# order based on strength
# reduce ? - no , applies a function to eachelement in list and reduces to a singe output ? 
#can get strength of hand by reducing on the list  is that fast
hands = [line.split() for line in open('test.txt')]
"""

# An array of each type containing tuples of hand and bet size ?
five_kind = f5
four_kind = f4
full_house = f3 f2
three_kind = f3
two_pair = f2 f2
one_pair = f2
high_card = f1 
"""
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

# create temp list which pulls in all which have
# sort all list 
# 2kq34 2
# 2kq34 2 
# 2kq34 1 
# 2kq34 1 
# 2kq34 1

# Sort the list based on the second index in each sublist, ie the strength
sorted_hands = sorted(hands, key=lambda x: int(x[2]))

temp = sorted()
# https://stackoverflow.com/questions/64576903/how-to-sort-the-list-in-custom-order-in-python
# Create a dictionary of cards to values to use for sorting
custom_order = {card:iterator for iterator,card in enumerate(['1','2','3','4','5','6','7','8','9','T','J','Q','K','A'])}

def customSort(l):
    l.sort(key=lambda c:custom_order.get(c, len(custom_order)))

print(customSort(['orange','purple','yellow','black','brown','pink','blue','green']))

my_list = ["apple", "banana", "kiwi", "orange", "grape"]

def custom_sort_key(value):
    # Define your custom sorting logic here
    # This function should return a value that will be used for comparison during sorting
    # Example: Sort by the length of the string in reverse order
    return len(value)

# Sort the list in place based on the custom_sort_key
my_list.sort(key=custom_sort_key, reverse=True)

print(my_list)
print(hands)