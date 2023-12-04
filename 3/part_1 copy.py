import re
#input_file = open("test.txt", "r")


string = 'geeksforgeeks'
lst = []
 
for letter in string:
    lst.append(letter)
 
print(lst)





# Open text file
with open("test.txt") as input_file:
    # readlines() will create a list of lines ['line1','line2']
    # lines = input_file.readlines()
    # print(lines)

    # List comprehension creates a list of lists [['line1'],['line2']].
    # This needs to change so it creates a list of lists, containing every char in the line [['l','i','n','e','1'],['...']]
    # lines2 = [line2.split() for line2 in input_file]
    # print(lines2)
    
    ###   ..3442..£..
    #  read line -> for each line split by char 
    # List Comprehension :: newlist = [%expression% for %item% in %iterable% if %condition% == True]
    lines = [line.split() for line in input_file]
    print(lines)
    li="test"
    newlines = [character for character in li]
    print(newlines)
    for row in lines:
        print("row ::{} ".format(row))
        for i in row:
            print(i)
        #newlist = row.split()
        #print(newlist)
    
    # For each line in the file, split by space and add each to array
    #lines = [line.split() for line in textFile]
    #For each line in the file, split by space and add each to array
#    lines = [c for character in textFile]

#print(lines)
