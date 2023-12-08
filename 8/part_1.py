with open('test.txt') as f:
    instructions = f.readline()
    f.readline()
    print(instructions)
    instructions_bin = [0 if c == 'L' else 1 for c in instructions]
    print(instructions_bin)
    node_list = f.readlines()

# Translation table is better than .replace as it looks for chars, not substrings, and can do multiple at once
translation_table = str.maketrans({'=': None, '(': None, ',': None, ')': None})
# Can this be made into a dict instead with tuple ? 
desert_map = [line.translate(translation_table).split() for line in node_list]
node = desert_map[1][instructions_bin[0]]
print(node)
#def move(node):
#    node = desert_map[node_index][instruction[instruction_iterator]]

#while node != 'ZZZ':
#    move(node)
