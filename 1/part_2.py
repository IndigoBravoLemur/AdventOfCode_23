import re
input_file = open("input.txt", "r")
lines = input_file.readlines()
total = 0

numbers = {
    "zero":"0", 
    "one":"1", 
    "two":"2", 
    "three":"3", 
    "four":"4", 
    "five":"5", 
    "six":"6",
    "seven":"7", 
    "eight":"8", 
    "nine":"9" 
}

for line in lines:
    # Grab first digit or digit-word
    first_digit = re.search("(\d|nine|eight|seven|six|five|four|three|two|one)", line)
    # Match any number of characters then the final following digit or digit-word
    last_digit = re.search(".*(\d|nine|eight|seven|six|five|four|three|two|one)", line)
    # Concatenating the strings together
    combined_digits = first_digit.group(1)+last_digit.group(1)
    # For each key/number in the dictionary replace it with the key-value, ie, its digit counterpart
    for key in numbers.keys():
        combined_digits = combined_digits.replace(key, numbers[key])
    # Add to total sum of digits
    total += int(combined_digits)

print(total)
