def main():
    # List comprehension for reading lines and stripping /n at the end
    # list = return list of the output of the expression line.rstrip() for each line (item) in the txt file (iterable).
    lines = [line.rstrip() for line in open('test2.txt')]

    # List Comprehension :: newlist = [%expression% for %item% in %iterable% if %condition% == True]
    # Create a list of the output of the expression 'character for....' for each line in the lines list
    #       The expression returns a list of characters for each character in the provided line 
    line_list = [[character for character in line] for line in lines]
    parts = []
    # For each line 
    for line_number in range(len(line_list)):
        #print(line_list[line_number])
        # For each character in line
        for character in range(len(line_list[line_number])):
            #print(line_list[line_number][c])
            check_is_part(line_list, line_number, character)

def check_is_part(line_list, line_number, index):
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if line_list[line_number][i].isdigit():
            char_is_digit = True

        # For each row above, current and below the current line number
        for i in range(-1,2):
            if i < 0 or i > len(line_list)-1:
                continue

            # Check characters of all adjacent to the given char
            # Starting at index-1, ending when it reaches index+2 (not including), add 1 each iteration
            for i in range(index-1,index+2,1):
                if i < 0 or i > len(line_list[line_number])-1:
                    continue                  
                if line_list[line_number][i] in special_characters:
                    print("adjacent to special char")
                    is_part=True
                else:
                    print("not adjacent to special char")

                #print(line_list[line_number][i])
            # If character is digit and is a part
            if char_is_digit and is_part:
                current_number += str(line_list[line_number][i])
            # Else if character is not a digit
            else:
                if current_number and is_part:
                    parts.append("orange")

                    

        # Current row
        # Below row

##  1 . . . .
##  . 4 . 4 5
##  3 . . . *
# 
# if number AND adjacent is part is true 
#    add to curr_num 
# else
#       if curr_num exists AND part is true
#           add curr_num to list of known good
#           set curr_num=""
#           set adjacent to false
#
#           
if __name__ == "__main__":
    main()
