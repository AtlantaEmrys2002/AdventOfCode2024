# Import Libraries
import numpy as np

# Read Files and Format Input
with open('day2input.txt') as file:
    lines = [line.rstrip().split() for line in file]

lines = [list(map(int, lines[x])) for x in range(len(lines))]

total = 0

for line in lines:
    differences = np.diff(np.array(line))

    if sorted(line) == line or sorted(line, reverse=True) == line:
        maximum_value = np.max(differences)
        minimum_value = np.min(differences)
        if maximum_value <= 3 and minimum_value >= 1:
            if line[0] < line[-1]:
                total += 1
        else:
            if maximum_value <= -1 and minimum_value >= -3:
                if line[0] > line[-1]:
                    total += 1

print(total)

# References
# Reading Python File - https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
