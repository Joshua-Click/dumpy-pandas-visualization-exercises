import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
print(sum_of_a)
# 55


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print (min_of_a)
# 1


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
print(max_of_a)
# 10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum_of_a / len(a)
print(mean_of_a)
# 5.5


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers 
# in the above list together

product_of_a = 1
for num in a:
    product_of_a *= num
   
print(product_of_a)
#  3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = [i**2 for i in a]
print(squares_of_a)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [num for num in a if num % 2 != 0]
print(odds_in_a)
# [1, 3, 5, 7, 9]


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [num for num in a if num % 2 == 0]
print(evens_in_a)
#[2, 4, 6, 8, 10]


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares 
## for this list of two lists.
# b = [
#     [3, 4, 5],
#     [6, 7, 8]
# ]

b = np.array([
    [3, 4, 5],
    [6, 7, 8]]
)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)

sum_of_b = b.sum()
print(sum_of_b)
# 33


# Exercise 2 - refactor the following to use numpy. 

# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b = b.min()

print(min_of_b)
# 3


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

#max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
print(max_of_b)
# 8


# Exercise 4 - refactor the following using numpy to find the mean of b

#mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = b.mean()
print(mean_of_b)
# 5.5 


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# 
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = b.prod()
print(product_of_b)
# 20160



# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
#         print(squares_of_b)

squares_of_b = np.square(b)
print(squares_of_b)
# [[ 9 16 25]
# [36 49 64]]


# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
# print(odds_in_b)

odds_in_b = b[b % 2 != 0]

print(odds_in_b)
# [3 5 7]


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)
# [4 6 8]


# Exercise 9 - print out the shape of the array b.

b_shape = b.shape
print(b_shape)
# (2, 3)


# Exercise 10 - transpose the array b.

b_transpose = np.transpose(b)
print(b_transpose)
# [[3 6]
#  [4 7]
#  [5 8]]


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b_reshape = np.reshape(b, -1)
print(b_reshape)

# Exercise 12 - reshape the array b to be a list of 6 lists, 
# each containing only 1 number (6 x 1)

b_shape_six = np.reshape(b, (6, 1))
print(b_shape_six)


## Setup 3
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# HINT, you'll first need to make sure that the "c" variable is a 
# numpy array prior to using numpy array methods.

# Exercise 1 - Find the min, max, sum, and product of c.

c_min = c.min()
print(c_min)
# 1

c_max = c.max()
print(c_max)
#9

c_sum = c.sum()
print(c_sum)
#45

c_prod = c.prod()
print(c_prod)
# 362880


# Exercise 2 - Determine the standard deviation of c.

c_std = c.std()
print(c_std)
# 2.581988897471611


# Exercise 3 - Determine the variance of c.

c_var = c.var()
print(c_var)
# 6.666666666666667


# Exercise 4 - Print out the shape of the array c

c_shape =np.shape(c)
print(c_shape)
# (3, 3)


# Exercise 5 - Transpose c and print out transposed result.

c_transpose = np.transpose(c)
print(c_transpose)
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]


# Exercise 6 - Get the dot product of the array c with c. 

c_dotprod = np.dot(c,c, out=None)
print(c_dotprod)
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]]


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. 
# Answer should be 261

sum_c_squared = np.sum(c * c_transpose)

print(sum_c_squared)
# 261


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.

print(np.prod(c * c_transpose))
# 131681894400


## Setup 4
# d = [
#     [90, 30, 45, 0, 120, 180],
#     [45, -90, -30, 270, 90, 0],
#     [60, 45, -45, 90, -45, 180]
# ]

d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])


# Exercise 1 - Find the sine of all the numbers in d

d_sine = np.sin(d)
print(d_sine)
# [[ 0.89399666 -0.98803162  0.85090352  0.          0.58061118 -0.80115264]
#  [ 0.85090352 -0.89399666  0.98803162 -0.17604595  0.89399666  0.        ]
#  [-0.30481062  0.85090352 -0.85090352  0.89399666 -0.85090352 -0.80115264]


# Exercise 2 - Find the cosine of all the numbers in d

d_cos = np.cos(d)
print(d_cos)
# [[-0.44807362  0.15425145  0.52532199  1.          0.81418097 -0.59846007]
#  [ 0.52532199 -0.44807362  0.15425145  0.98438195 -0.44807362  1.        ]
#  [-0.95241298  0.52532199  0.52532199 -0.44807362  0.52532199 -0.59846007]]


# Exercise 3 - Find the tangent of all the numbers in d

d_tan = np.tan(d)
print(d_tan)
# [[-1.99520041 -6.4053312   1.61977519  0.          0.71312301  1.33869021]
#  [ 1.61977519  1.99520041  6.4053312  -0.17883906 -1.99520041  0.        ]
#  [ 0.32004039  1.61977519 -1.61977519 -1.99520041 -1.61977519  1.33869021]]


# Exercise 4 - Find all the negative numbers in d



# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2