
# List comprehension for reading lines and stripping /n at the end
# list = return list of the output of the expression line.rstrip() for each line (item) in the txt file (iterable).
lines = [line.rstrip() for line in open('test.txt')]

# List Comprehension :: newlist = [%expression% for %item% in %iterable% if %condition% == True]
# Create a list of the output of the expression 'character for....' for each line in the lines list
#       The expression returns a list of characters for each character in the provided line 
line_list = [[character for character in line] for line in lines]

# Get beginning of int, end of int
print(len(line_list[1]))

# For each line 
for i in range(len(line_list)):
    # For each character in line
    for c in range(len(line_list)):
        if c.isdigit():
            print("ok")

"""
# Open text file
#with open("test.txt") as input_file:
bl = []
for line in input_file:
    l = []
    line = line.rstrip('\n')
    #print(line)
    for letter in line:
        l.append(letter)
    #print(l)
    bl.append(l)
print(bl)




"""

# for each character in the 2d array check its position
