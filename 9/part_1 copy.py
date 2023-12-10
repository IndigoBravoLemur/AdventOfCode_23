#sequences = [line.split() for line in open('test.txt')]
# Using a tuple of lists because maybe its faster and also why not
sequences = tuple((line.split() for line in open('test.txt')))

print(sequences)
for sequence in sequences:
    current_sequence_list = []
    current_sequence_list.append(sequence)
    print(current_sequence_list)
    
"""


data = [[*map(int, s.split())] for s in open('data.txt')]

def f(l):
    diffs = [b-a for a,b in zip(l, l[1:])]
    return l[-1] + f(diffs) if l else 0

for dir in 1, -1:
    print(sum(f(l[::dir]) for l in data))
"""