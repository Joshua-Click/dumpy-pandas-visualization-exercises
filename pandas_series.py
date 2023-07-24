import pandas as pd
import numpy as np




# Exercise Part I

# Use pandas to create a Series named fruits from the following list:

#["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", 
# "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", 
# "gooseberry", "papaya"]

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruit_series = pd.Series(fruits)

# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.

fruit_series.count()
# 17


# 2. Output only the index from fruits.

fruit_series.index.values
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])


# 3.Output only the values from fruits.

fruit_series.values
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
#        'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
#        'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
#        'papaya'], dtype=object)


# 4. Confirm the data type of the values in fruits.

fruit_series.dtype
# dtype('O')


# 5. Output only the first five values from fruits. Output the last three values. 
#    Output two random values from fruits.

fruit_series.head()
# 0          kiwi
# 1         mango
# 2    strawberry
# 3     pineapple
# 4    gala apple
# dtype: object

fruit_series.tail(3)
# 14    blackberry
# 15    gooseberry
# 16        papaya
# dtype: object

fruit_series.sample(2)
# 15    gooseberry
# 11          kiwi
# dtype: object


# 6. Run the .describe() on fruits to see what information it returns when called on a 
#    Series with string values.

fruit_series.describe()
# count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object


# 7. Run the code necessary to produce only the unique string values from fruits.

fruit_series.unique()
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
#        'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
#        'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)


# 8. Determine how many times each unique string value occurs in fruits.

fruit_count = pd.value_counts(fruit_series)
# kiwi                4
# mango               2
# strawberry          1
# pineapple           1
# gala apple          1
# honeycrisp apple    1
# tomato              1
# watermelon          1
# honeydew            1
# blueberry           1
# blackberry          1
# gooseberry          1
# papaya              1
# dtype: int64


# 9. Determine the string value that occurs most frequently in fruits.

fruit_count.idxmax()

fruit_series.value_counts().head(1)
# kiwi    4
# dtype: int64

# 10. Determine the string value that occurs least frequently in fruits.



fruit_series.value_counts().nsmallest(n=1, keep='all')
# strawberry          1
# pineapple           1
# gala apple          1
# honeycrisp apple    1
# tomato              1
# watermelon          1
# honeydew            1
# blueberry           1
# blackberry          1
# gooseberry          1
# papaya              1
# dtype: int64


# Exercise Part II
# Explore more attributes and methods while you continue to work with the fruits Series.

# 1. Capitalize all the string values in fruits.

fruit_series.str.capitalize()
# 0                 Kiwi
# 1                Mango
# 2           Strawberry
# 3            Pineapple
# 4           Gala apple
# 5     Honeycrisp apple
# 6               Tomato
# 7           Watermelon
# 8             Honeydew
# 9                 Kiwi
# 10                Kiwi
# 11                Kiwi
# 12               Mango
# 13           Blueberry
# 14          Blackberry
# 15          Gooseberry
# 16              Papaya
# dtype: object


# 2. Count the letter "a" in all the string values (use string vectorization).

fruit_series.str.count('a')
# 0     0
# 1     1
# 2     1
# 3     1
# 4     3
# 5     1
# 6     1
# 7     1
# 8     0
# 9     0
# 10    0
# 11    0
# 12    1
# 13    0
# 14    1
# 15    0
# 16    3
# dtype: int64


# 3. Output the number of vowels in each and every string value.

vowels = list('aeiou')
fruit_series.isin(vowels).value_counts()
# False    17
# dtype: int64


# 4. Write the code to get the longest string value from fruits.

fruit_series.str.len().max()
#16


# 5. Write the code to get the string values with 5 or more letters in the name.

fruit_series[fruit_series.str.len() >= 5]
# 1                mango
# 2           strawberry
# 3            pineapple
# 4           gala apple
# 5     honeycrisp apple
# 6               tomato
# 7           watermelon
# 8             honeydew
# 12               mango
# 13           blueberry
# 14          blackberry
# 15          gooseberry
# 16              papaya
# dtype: object


# 6. Find the fruit(s) containing the letter "o" two or more times.

fruit_series[fruit_series.str.count('o') >= 2]
# 6         tomato
# 15    gooseberry
# dtype: object


# 7.Write the code to get only the string values containing the substring "berry".

fruit_series[fruit_series.str.contains('berry')]
# 2     strawberry
# 13     blueberry
# 14    blackberry
# 15    gooseberry
# dtype: object


# 8. Write the code to get only the string values containing the substring "apple".
fruit_series[fruit_series.str.contains('apple')]
# 3           pineapple
# 4          gala apple
# 5    honeycrisp apple
# dtype: object


# 9. Which string value contains the most vowels?






# Exercises Part III

# Use pandas to create a Series named letters from the following string. 
# The easiest way to make this string into a Pandas series is to use list 
# to convert each individual letter into a single string on a basic Python list.

letter = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letter_series = pd.Series(letter)
# 1. Which letter occurs the most frequently in the letters Series?

pd.value_counts(letter_series).head(1)
# y    13
# dtype: int64


# 2. Which letter occurs the Least frequently?
pd.value_counts(letter_series).tail(1)
# l    4
# dtype: int64


# 3. How many vowels are in the Series?

letter_series.isin(vowels).value_counts()

# True      34
# dtype: int64

# 4. How many consonants are in the Series?
letter_series.isin(vowels).value_counts()
#False    166

# 5. Create a Series that has all of the same letters but uppercased.

cap_series = letter_series.str.upper()
cap_series


# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

six_most = pd.value_counts(letter_series).head(6)
six_most.plot.bar().set(xlabel = 'Letter', ylabel = "Frequency")


# Use pandas to create a Series named numbers from the following list:

numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
num_series = pd.Series(numbers)


# 1. What is the data type of the numbers Series?

num_series.dtype
# dtype('O')


# 2. How many elements are in the number Series?

num_series.count()
# 20

# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert 
#    the numbers Series to a numeric data type.

num_series_float = num_series.str.replace('$', ' ').str.replace(',', '').astype('float')
num_series_float

# 4. Run the code to discover the maximum value from the Series.

num_series_float.nlargest(1)
# 11    4789988.17
# dtype: float64

# 5. Run the code to discover the minimum value from the Series.

num_series_float.nsmallest(1)
# 1    278.6
# dtype: float64

# 6. What is the range of the values in the Series?

num_max = num_series_float.nlargest(1) 
num_min = num_series_float.nsmallest(1)
num_range = num_max - num_min
print(num_range)


# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

num_bins_series = pd.cut(num_series_float, 4)
nb = num_bins_series.value_counts()


# 8 .Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

nb.plot.bar().set(xlabel='Values', ylabel= 'Frequency')



# Use pandas to create a Series named exam_scores from the following list:

scores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series(scores)

exam_scores.dtype
dtype('int64')

# 1. How many elements are in the exam_scores Series?

exam_scores.count()
# 20

# 2. Run the code to discover the minimum, the maximum, the mean, and the median 
#    scores for the exam_scores Series.

exam_scores.describe()
# count    20.000000
# mean     78.150000
# std      11.352139
# min      60.000000
# 25%      70.500000
# 50%      79.000000
# 75%      85.250000
# max      96.000000
# dtype: float64


# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

exam_scores.plot.hist().set(xlabel='Grade', ylabel='Frequency')

# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
#    Add the necessary points to the highest grade to make it 100, and add the same number of 
#    points to every other score in the Series as well.

# need (100 - max) + every other score

curved_grades = (100 - exam_scores.max()) + exam_scores

print(curved_grades)

# 0      64
# 1      90
# 2      79
# 3      66
# 4      97
# 5      75
# 6      64
# 7      87
# 8      99
# 9      82
# 10     69
# 11     76
# 12     73
# 13     85
# 14    100
# 15     84
# 16     89
# 17     96
# 18     86
# 19     82
# dtype: int64


# 5. Use a method to convert each of the numeric values in the curved_grades 
# Series into a categorical value of letter grades. 
# For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.




# 6. Plot your new categorical letter_grades Series in a meaninful way and include 
#    a title and axis labels.


