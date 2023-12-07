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
        print("Checking line number {}".format(line_number))
        # For each character in line
        for index in range(len(line_list[line_number])):
            print("Checking character {}".format(line_list[line_number][index]))
            is_part = False
            special_characters = "!@#$%^&*()-+?_=,<>/"

            if line_list[line_number][index].isdigit():
                char_is_digit = True

            # For each row above, current and below the current line number
            for i in range(-1,2):
                print("checkng line {}".format(i))
                current_number = ""
                # Skip if at the beginning or end of line
                if i < len(line_list[line_number+i]) or i > len(line_list)-1:
                    continue

                # Check characters of all adjacent to the given char
                # Starting at index-1, ending when it reaches index+2 (not including), add 1 each iteration
                for i in range(index-1,index+2,1):
                    if i < 0 or i > len(line_list[line_number])-1:
                        continue                  
                    if line_list[line_number][i] in special_characters:
                        print("{} adjacent to special char".format(line_list[line_number][i]))
                        is_part=True
                    #else:
                        #print("{} not adjacent to special char".format(line_list[line_number][i]))
            
            if is_part:
                print("{} adjacent to special char".format(line_list[line_number][index]))
            # If character is digit add to current digit list
            if char_is_digit:
                current_number += str(line_list[line_number][index])
            # Else if character is not a digit
            else:
                if current_number and is_part:
                    parts.append(current_number)
                    current_number = ""

                        

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
