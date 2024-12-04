import re

# part 1
input = ""
with open('input.txt') as f:
    input = f.read()

matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", input)

total = 0

for pair in matches:
    total += int(pair[0]) * int(pair[1])

print("Pt 1: ", total)

# part 2
total = 0
matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\)|don\'t\(\))", input)
cond = False
for pair in matches:
    if pair[2] == "don't()":
        cond = True
        continue
    elif pair[2] == "do()":
        cond = False
        continue
    if cond is False:
        total += int(pair[0]) * int(pair[1])

print("pt 2: ", total)  

