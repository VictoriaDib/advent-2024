import numpy as np

#pt1
with open("input.txt") as f:
    grid = [list(line.strip()) for line in f]

npGrid = np.array(grid)
rows, cols = npGrid.shape

find = "XMAS"
len = len(find)
count = 0


neighbors = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1)     ,     ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def xmas(row, col, x, y):
    for i in range(len):
        y2 = row + i * x
        x2 = col + i * y
        if not (0 <= y2 < rows and 0 <= x2 < cols) or npGrid[y2][x2] != find[i]:
            return False
    return True

for row in range(rows):
    for col in range(cols):
        for y, x in neighbors:
            if xmas(row, col, y, x):
                count += 1


print("pt1: ", count)

#pt2 