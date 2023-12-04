def main():
    # List comprehension for reading lines and stripping /n at the end
    # list = return list of the output of the expression line.rstrip() for each line (item) in the txt file (iterable).
    lines = [line.rstrip() for line in open('test2.txt')]

    # List Comprehension :: newlist = [%expression% for %item% in %iterable% if %condition% == True]
    # Create a list of the output of the expression 'character for....' for each line in the lines list
    #       The expression returns a list of characters for each character in the provided line 
    line_list = [[character for character in line] for line in lines]

    # For each line 
    for line_number in range(len(line_list)):
        #print(line_list[line_number])
        # For each character in line
        for character in range(len(line_list[line_number])):
            #print(line_list[line_number][c])
            check_is_part(line_list, line_number, character)

def check_is_part(line_list, line_number, index):
        special_characters = "!@#$%^&*()-+?_=,<>/"

        # Above row
        # Check character diagonally to the left, above and diagonally right of the char
        for i in range(index-1,index+2,1):
            if i < 0 or i > len(line_list[line_number])-1:
                continue               
            if line_list[line_number][i] in special_characters:
                print("adjacent to special char")
            else:
                print("not adjacent to special char")
            print(line_list[line_number][i])
            is_part=True
        # Current row
        # Below row


if __name__ == "__main__":
    main()

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
