import pandas as pd
import numpy as np






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

fruit_count.max()

# 10. Determine the string value that occurs least frequently in fruits.

fruit_count.min()