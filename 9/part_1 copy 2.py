# For each line in the file, split the lines and return a list of strings for each line
#data = [line.split() for line in open('test.txt')]
# For each line in the file, use the map function on the list (iterable) of strings from that line 
# # ...  to make each string an int. This returns a list of int's instead of strings from the file
# # what is the * doing ?
sequences = [[*map(int, line.split())] for line in open('test.txt')]

def get_next_num(sequence):
    new_sequence =[]
    # For the length of the given sequence -1
    for i in range(len(sequence)-1):
        # Add to the new sequence the difference between the current index and the one ahead of it 
        new_sequence.append(sequence[i+1]-sequence[i])
    # If all elements in the new list are 0, add all 
    if all(num == 0 for num in new_sequence):
        get_next_num(new_sequence)



for sequence in sequences:
    get_next_num(sequence)
   
