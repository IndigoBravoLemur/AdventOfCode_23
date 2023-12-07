def main():
    # List comprehension for reading lines and stripping /n at the end
    # list = return list of the output of the expression line.rstrip() for each line (item) in the txt file (iterable).
    lines = [line.rstrip() for line in open('test.txt')]

    # List Comprehension :: newlist = [%expression% for %item% in %iterable% if %condition% == True]
    # Create a list of the output of the expression 'character for....' for each line in the lines list
    #       The expression returns a list of characters for each character in the provided line 
    line_list = [[character for character in line] for line in lines]
    parts = []
    # For each line 
    for line_number in range(len(line_list)):
        print("Checking line {} for part numbers".format(line_number))
        current_number = ""
        is_part = False
        # For each character in line
        for index in range(len(line_list[line_number])):
            print("--Checking characters surrounding {}".format(line_list[line_number][index]))
            
            special_characters = "!@#$%^&*()-+?_=,<>/"

            if line_list[line_number][index].isdigit():
                #print("----Character is digit")
                current_number = current_number + str(line_list[line_number][index])
                print(current_number)
            # If it is not a digit and there is a current number with a part associated add it to the list of parts. Then reset current number
            else:
                #print("----Character is not a digit, skipping")
                if current_number and is_part:
                    #print(current_number + " is adjacent to a special character")
                    parts.append(current_number)
                current_number = ""
                is_part = False
                continue

            # For each row above, current and below the current line number
            for line_iterator in range(-1,2):
                print("Checking line {}".format(line_iterator))
                lineindex = line_number + line_iterator
                # Skip if at the beginning or end of line
                if lineindex < 0 or lineindex > len(line_list)-1:
                    print("----Skipping line as it is out of range")
                    continue
                #print("index :{} ; iterator:{}".format(index,adjacent_iterator)) 
                # Check characters of all adjacent to the given char
                # Starting at index-1, ending when it reaches index+2 (not including), add 1 each iteration
                for adjacent_iterator in range(index-1,index+2,1):
                    #print("index :{} ; iterator:{}".format(index,adjacent_iterator))
                    if adjacent_iterator < 0 or adjacent_iterator > len(line_list[line_number])-1:
                        #print("----Skipping character as it is out of range")
                        continue
                    print("----Checking char {}".format(line_list[lineindex][adjacent_iterator]))                
                    if line_list[lineindex][adjacent_iterator] in special_characters:
                        print("----{} is a special char".format(line_list[lineindex][adjacent_iterator]))
                        is_part=True
            
            #if is_part:
            #    print("----{} adjacent to special char".format(line_list[line_number][index]))
            
        # At the end of the line, submit current number string to list if exists and is part
        if current_number and is_part:
            parts.append(current_number)
            current_number = ""
            is_part = False

    print(parts)
    #(or) -- [int(x) for x in xs]
    intparts = map(int, parts)
    partssum = sum(intparts)
    print(partssum)

if __name__ == "__main__":
    main()
