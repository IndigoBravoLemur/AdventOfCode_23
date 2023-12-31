with open('input.txt') as f:
    instructions = f.readline()
    f.readline()
    instructions_bin = [0 if c == 'L' else 1 for c in instructions.strip()]
    node_list = f.readlines()

translation_table = str.maketrans({'=': None, '(': None, ',': None, ')': None})
desert_map = [line.translate(translation_table).split() for line in node_list]
desert_dict = {items[0]: tuple(items[1:]) for items in desert_map}
#desert_dict = {line.translate(translation_table).split()[0]: tuple(line.translate(translation_table).split()[1:]) for line in node_list}
### line.translate(translation_table).split()[0] extracts the first item for the key.
### tuple(line.translate(translation_table).split()[1:]) extracts the rest of the items as a tuple for the value.

node = "AAA"
ii=0
steps=0
def move(node, ii):
    global steps
    try:
        node = desert_dict[node][instructions_bin[ii]]
        ii+=1
        steps += 1 
    except IndexError:
        ii = 0
        return node, ii 
    return node, ii

while node != 'ZZZ':   
    node, ii = move(node,ii)
print(steps)
