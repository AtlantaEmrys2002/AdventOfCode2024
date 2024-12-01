import numpy as np

file = open('day1input.txt', 'r')

first_line = file.readline().split()
print(first_line)

list1 = [int(first_line[0])]
list2 = [int(first_line[1])]

while True:
    first_line = file.readline().split()
    if first_line == []:
        break
    else:
        line_int = first_line
        line1, line2 = line_int[0], line_int[1]
        list1.append(int(line1))
        list2.append(int(line2))

list1 = np.sort(np.asarray(list1))
list2 = np.sort(np.asarray(list2))
difference = np.subtract(np.copy(list1), np.copy(list2))

total = np.subtract(np.sort(np.asarray(list1)), np.sort(np.asarray(list2)))

# print(np.sum(np.abs(difference)))

similarity = 0

for val in list1:
    # print(val)
    occurrences = 0
    if val in list2:
        for k in list2:
            if k == val:
                occurrences += 1
    similarity += (val * occurrences)

print(similarity)