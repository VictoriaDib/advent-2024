import re

input = ""
with open('input.txt') as f:
    input = f.read()

matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", input)

total = 0

for pair in matches:
    total += int(pair[0]) * int(pair[1])

print(total)