import re
input_file = open("input.txt", "r")
lines = input_file.readlines()
total = 0
for line in lines:
    first_digit = re.search("^[^\d]*(\d)", line)
    last_digit = re.search(".*(\d)", line)
    combined_digits = first_digit.group(1)+last_digit.group(1)
    total += int(combined_digits)
print(total)
