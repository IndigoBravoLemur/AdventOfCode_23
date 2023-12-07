def main():
    lines = [line.rstrip() for line in open('test2.txt')]
    line_list = [[character for character in line] for line in lines]

    for line_number in range(len(line_list)):    
        result = [check_is_part(line_list, line_number, character) for character in range(len(line_list[line_number]))]

    print(result)

def check_is_part(line_list, line_number, index):
        special_characters = "!@#$%^&*()-+?_=,<>/"
        for i in range(index-1,index+2,1):
            if i < 0 or i > len(line_list[line_number])-1:
                continue               
            if line_list[line_number][i] in special_characters:
                print("adjacent to special char")
            else:
                print("not adjacent to special char")
            print(line_list[line_number][i])
            is_part=True

if __name__ == "__main__":
    main()
