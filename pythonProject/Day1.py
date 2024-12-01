# Import Libraries
import numpy as np

# Read File and Format Input
file = open('day1input.txt', 'r')
first_line = file.readline().split()

list1 = [int(first_line[0])]
list2 = [int(first_line[1])]

while True:
    first_line = file.readline().split()
    if not first_line:
        break
    else:
        line_int = first_line
        line1, line2 = line_int[0], line_int[1]
        list1.append(int(line1))
        list2.append(int(line2))

# Problem 1
total = np.sum(np.abs(np.subtract(np.sort(np.asarray(list1)), np.sort(np.asarray(list2)))))

# Problem 2
similarity = np.sum(np.asarray([int(np.count_nonzero(list2 == np.int64(val))) * val for val in list1]))

print(total)
print(similarity)