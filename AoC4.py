#PART 1 XMAS
import re
xmas = 0
columns = []  # needed for vertical control

diag_LtoR = []  # needed for diagonal left to right control
diag_RtoL = []  # '' right to left control

with open("input.txt", 'r') as file:
    
    # no no index out of order no more
    lines = [line.strip() for line in file.readlines()]
    length = max(len(line) for line in lines)
    lines = [line.ljust(length, '.') for line in lines]

    if lines:
        columns = [''] * length

        for _ in range(2):  #to be sure of reversed patterns
            pattern = "XMAS" if _ == 0 else "SAMX"

            # horizontal control -----------------------------
            for i in range(len(lines)):
                matches = re.findall(pattern, lines[i])
                xmas += len(matches)
                lines[i] = re.sub(pattern, '....', lines[i])

            # vertical control -----------------------------
            columns = [''.join(row[i] for row in lines) for i in range(length)]
            for i in range(len(columns)):
                matches = re.findall(pattern, columns[i])
                xmas += len(matches)
                columns[i] = re.sub(pattern, '....', columns[i])

            for i in range(length):
                for j in range(len(lines)):
                    if i < len(lines[j]):
                        lines[j] = lines[j][:i] + columns[i][j] + lines[j][i + 1:]

            # diagonal control LEFT to RIGHT -----------------------------
            diag_LtoR = []
            for y, line in enumerate(lines):  # gives numbers to the lines
                for x in range(length):
                    diagonal = []
                    i, j = y, x  # i goes vertically and j goes horizontally
                    while i < len(lines) and j < length:
                        diagonal.append(lines[i][j])
                        i += 1
                        j += 1
                    if diagonal:
                        diag_LtoR.append((y, x, ''.join(diagonal)))

            for y, x, diagonal in diag_LtoR:
                matches = re.findall(pattern, diagonal)
                xmas += len(matches)
                updated_diag = re.sub(pattern, '....', diagonal)
                i, j = y, x
                for c in updated_diag:
                    if i < len(lines) and j < length:
                        lines[i] = lines[i][:j] + c + lines[i][j + 1:]
                        i += 1
                        j += 1

            # diagonal control RIGHT TO LEFT -----------------------------
            diag_RtoL = []
            for y, line in enumerate(lines):
                for x in range(length):
                    diagonal = []
                    i, j = y, x
                    while i < len(lines) and j >= 0:  # avoids j ending the line and going on
                        diagonal.append(lines[i][j])
                        i += 1
                        j -= 1
                    if diagonal:
                        diag_RtoL.append((y, x, ''.join(diagonal)))

            for y, x, diagonal in diag_RtoL:
                matches = re.findall(pattern, diagonal)
                xmas += len(matches)
                updated_diag = re.sub(pattern, '....', diagonal)
                i, j = y, x
                for c in updated_diag:
                    if i < len(lines) and j >= 0:
                        lines[i] = lines[i][:j] + c + lines[i][j + 1:]
                        i += 1
                        j -= 1

# end ----------------------------- I have a headache now, yey
print(xmas)
