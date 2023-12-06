import re
with open('i_c.txt', 'r') as file:
    data = file.read()

pattern = r'Card\s+\d+:\s+(\d+[\s\d]+)\s*\|\s*(\d+[\s\d]+)'
matches = re.search(pattern, data)

if matches:
    set1 = re.split(r'\s+', matches.group(1)) if matches.group(1) else []
    set2 = re.split(r'\s+', matches.group(2)) if matches.group(2) else []
    print("Set 1:", set1)
    print("Set 2:", set2)
else:
    print("No match found.")