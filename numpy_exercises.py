import numpy as np


#use the following code for the questions below
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

neg_a = np.sum(a < 0)
print(neg_a)
# 4

under_zero = a < 0
print( len(a[under_zero]))
# 4 

# 2. How many positive numbers are there?

pos_a = np.sum(a >= 0)
print(pos_a)
# 8


# 3. How many even positive numbers are there?

even_a = (a % 2 == 0) & (a > 0)
print(len(a[even_a]))
# 3


# 4. if you were to add 3 to each data point, how many positive numbers would there be?

plus_three = a + 3
print((plus_three))

neg_a_three = np.sum(plus_three < 0)
print(neg_a_three)
# 2


# 5. If you squared each number, what would the new mean and standard deviation be?

square_it = a ** 2
get_mean = square_it.mean()
print(get_mean)
# 74.0

get_stdev = square_it.std()
print(get_stdev)
# 144.02


# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set. 
print(a)
# [ 4 10 12 23 -2 -1  0  0  0 -6  3 -7]

center_func = a - a.mean()

print(center_func)
# [  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.]

# found on the net and wanted to see it
centaur = lambda x: x - x.mean()
data_cent = centaur(a)
print(data_cent)
# [  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.]


# 7. Calculate the z-score for each data point. 
# Recall that the z-score is given by: z = (x-u)/o

z_score = (a - a.mean()) / a.std()

print(z_score)
# [ 0.12403473  0.86824314  1.11631261  2.48069469 -0.62017367 -0.49613894
# -0.3721042  -0.3721042  -0.3721042  -1.11631261  0.         -1.24034735]
