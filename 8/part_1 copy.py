#with open('input.txt') as f:
#    instructions = f.readline().strip()
    
#    print(ins)
#    latter=f.readline()
#    print(latter)

# Translation table is better than .replace as it looks for chars, not substrings, and can do multiple at once
translation_table = str.maketrans({'=': None, '(': None, ',': None, ')': None})
testre="hello)here=there("
testre = testre.translate(translation_table)
print(testre)

input = [line.translate(translation_table).split for line in open('test.txt')]
for s in input:
    print(s)
#input2 = [line for line in open("test.txt")]
#input3 = [s for s:=line.translate(translation_table).split for line in open('test.txt')]

print(input)
#print(input2)
#print(input3)
#input = [line.split() for line in open('test.txt')]
#print(input[0])
#for u in input[0]:
#    print(u)
#instructions = [0 if c == 'L' else 1 for c in input[0][0]]
#print(input)
#for i in input[3:]:
#    print("thingb")
# Split by newline
# define calling fuction?
# Instruction 