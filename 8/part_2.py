# This works to brute force but is unreasonable to complete the task with. needs the LCM solution
with open('input.txt') as f:
    instructions = f.readline()
    f.readline()
    instructions_bin = [0 if c == 'L' else 1 for c in instructions.strip()]
    node_list = f.readlines()

translation_table = str.maketrans({'=': None, '(': None, ',': None, ')': None})
desert_map = [line.translate(translation_table).split() for line in node_list]
desert_dict = {items[0]: tuple(items[1:]) for items in desert_map}
nodes = [node for node in desert_dict if (node[2]=='A')]
ii=0
steps=0

def move(nodes):
    global steps
    global ii
    try:
        for i,node in enumerate(nodes):
            nodes[i] = desert_dict[node][instructions_bin[ii]]
        ii+=1
        steps += 1 
    except IndexError:
        ii = 0
        return nodes
    return nodes
print(nodes)
while [node for node in nodes if (node[2]!='Z')]:
    nodes = move(nodes)
    print(nodes)

print(steps)
