import re

xmas = 0

grid = []
single_line = []
remover = 0  # for utf-8 characters

# filling all the grid ----------------------------------------------------------
with open("input.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        remover += 1
        single_line = line
        # removing \n and utf-8 characters
        single_line = re.findall(".", single_line)
        if remover == 1:
            single_line = single_line[1:len(single_line)]
        grid.append(single_line)

# making control squares ----------------------------------------------------------
buffer = []
square = []
all_squares = []
stop = len(grid) - 3  # limit
for row in range(stop):
    for col in range(stop):
        buffer = []
        for i in range(4):
            buffer.append(grid[row + i][col:col + 4])  # takes a 4x4 square
        square = buffer
        all_squares.append(square)

# checking for patterns ----------------------------------------------------------
counter = 0
to_check = ""
pattern = "XMAS"
pattern_rev = "SAMX"

# horizontal WORKS ---------------------------------------------
tot_lines = len(grid)
for s in all_squares:
    to_check = "".join(s[0])
    if to_check == pattern:
        counter += 1
    if to_check == pattern_rev:
        counter += 1
control_lines = []
line = tot_lines - 3
stop = len(grid[tot_lines - 1]) - 3  # limit
while line <= tot_lines - 1:
    for char in range(stop):
        buffer = []
        for i in range(4):
            buffer.append(grid[line][char + i])  # takes a 4 char line
        control_line = buffer
        control_lines.append(control_line)
    line = line + 1
for cl in control_lines:
    to_check = "".join([cl[i] for i in range(4)])
    if to_check == pattern:
        counter += 1
    if to_check == pattern_rev:
        counter += 1

# vertical WORKS ---------------------------------------------
for c in all_squares:
    to_check = "".join([c[i][0] for i in range(4)])
    if to_check == pattern:
        counter += 1
    if to_check == pattern_rev:
        counter += 1
line_len = len(grid[tot_lines - 1])
flag = line_len - 3
control_cols = []
for col in range(flag, line_len):
    for row in range(tot_lines - 3):
        buffer = []
        for i in range(4):
            buffer.append(grid[row + i][col])
        to_check = "".join(buffer)
        if to_check == "XMAS":
            counter += 1
            print("+1")
        if to_check == "SAMX":
            counter += 1
            print("+1")

# diagonal left to right WORKS ---------------------------------------------
for c in all_squares:
    to_check = "".join([c[i][i] for i in range(4)])
    if to_check == pattern:
        counter += 1
    if to_check == pattern_rev:
        counter += 1

# diagonal right to left WORKS ---------------------------------------------
for c in all_squares:
    to_check = "".join([c[i][3 - i] for i in range(4)])
    if to_check == pattern:
        counter += 1
    if to_check == pattern_rev:
        counter += 1

print("---------")
print(counter)





