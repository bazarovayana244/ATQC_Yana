###Using lambda multiply each number of given list with a given number###
x = [1, 2, 3, 4]
y = 3

multiply = lambda a: a * y
result = [multiply(a) for a in x]
print(result)

# -----------------------------------------------------------------------------------------------------------------------#

###Using lambda check if a number in the given list is odd. Print True if the number is even and False if not for each element###
x = [1, 2, 3, 4]

check = lambda a: True if a % 2 == 0 else False
for even in x:
    print(check(even))

# -----------------------------------------------------------------------------------------------------------------------#

###Using lambda extract year, month, day and time from datetime object###
from datetime import datetime #import from datetime module

dt = datetime(2025, 9, 21, 23, 45, 20)

x = lambda a: (a.year, a.month, a.day, a.hour, a.minute, a.second)
year, month, day, hour, minute, second = x(dt)
print(year, month, day, hour, minute, second)

# -----------------------------------------------------------------------------------------------------------------------#

###Using lambda to double each item in a list using map()###
x = [1, 2, 3, 4]

double = list(map(lambda a: a * 2, x))
print(double)

# -----------------------------------------------------------------------------------------------------------------------#

###Using lambda filter out only odd items from the list using filter()###
x = [1, 2, 3, 4]

odd = list(filter(lambda a: a % 2 != 0, x))
print(odd)

# -----------------------------------------------------------------------------------------------------------------------#