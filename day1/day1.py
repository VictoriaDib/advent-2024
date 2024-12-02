total = 0
left = []
right = []

# pt1
with open('input-example.txt') as f:
    for line in f:
        s = tuple(line.strip("\n").split("   "))
        left.append(int(s[0]))
        right.append(int(s[1]))

left.sort()
right.sort()

for i, j in zip(left, right):
    total += abs(i-j)

print("pt 1: ", total)

# pt2
total = 0

for i in left:
    similarity = right.count(i)
    total += i * similarity

print("pt 2: ", total)