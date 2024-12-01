# Import Libraries
import numpy as np

# Read Files and Format Input
data = np.delete(np.genfromtxt('day1input.txt', delimiter=' '), [1, 2], 1).transpose()
list1, list2 = data[0], data[1]

# Problem 1
total = np.sum(np.abs(np.subtract(np.sort(np.asarray(list1)), np.sort(np.asarray(list2)))))

# Problem 2
similarity = np.sum(np.asarray([int(np.count_nonzero(list2 == np.int64(val))) * val for val in list1]))

print(total)
print(similarity)