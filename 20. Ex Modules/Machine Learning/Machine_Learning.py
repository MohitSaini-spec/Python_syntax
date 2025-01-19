# Numerical data are numbers, and can be split into two numerical categories:

# Discrete Data
# - counted data that are limited to integers. Example: The number of cars passing by.
# Continuous Data
# - measured data that can be any number. Example: The price of an item, or the size of an item
# Categorical data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.

# Ordinal data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.

# By knowing the data type of your data source, you will be able to know what technique to use when analyzing them.

# You will learn more about statistics and analyzing data in the next chapters.


import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)      #numpy of standred devation

print(x) 



# m,m,m , standred devation , varience

# mean of each
# diffrence for each value
# sq them
# 