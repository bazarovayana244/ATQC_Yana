###Using a list comprehension, create a new list from the given, which contains only the negative numbers from the list, as integers###
list_numbers = [1, 2.0, -3, -5.6, 7, 567, -435]
negative = [x for x in list_numbers if x < 0]
print(negative)


###Using a list comprehension, create a new list extracting specified size of strings from the given list of strings###
list_str = ["Hello World", "The world is mine", "Enjoy the silence"]
size = 11
new_list = [x for x in list_str if len(x) == 11]
print(new_list)


### Using a list comprehension, create a new list with the numbers divisible by thirteen###
numbers = [2, 13, 25, 39, 45.4, 91]
divide = [x for x in numbers if x % 13 == 0]
print(divide)


###Using a list comprehension, create a new list of a given list of names after removing the names that starts with lowercase###

names = ["John", "Yana", "mary", "Alice", "bob"]
case = [x for x in names if x[0].isupper()]
print(case)


###Using a list comprehension, find numbers within a given range where every number is divisible by every digit it contains###

start = 1
end = 100

result = [x for x in range(start, end +1)
          if all(int(a) != 0 and x % int(a) == 0 for a in str(x))]
print(result)
