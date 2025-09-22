###Create int, float and string variables with different values, compare them, print results and explain results###
a = 5
b = 8.25
c = "52"

# int and float can be compared
print(a == b)
print(a < b)
print(a > b)

# int and float can not be compared with str using "==" (but "==" works like "is" no error)
print(a == c)
print(b == c)

# int and float can not be compared with str using "<" or ">"- TypeError

# -----------------------------------------------------------------------------------------------------------------------#

###Using 'Casting' create int, float, str variables with value 5. Divide each variable by 2. Print results, explain results###
a = int(5)
b = float(5)
c = str(5)

# Divide each variable by 2
divide_a = a / 2
divide_b = b / 2

# Print results
print(divide_a)
print(divide_b)

# Cannot divide str. Should convert str to int
c = int(c)
divide_c = int(c) / 2
print(divide_c)
print(int(c) / 2)

# -----------------------------------------------------------------------------------------------------------------------#

###Using "Casting" create 3 int variables with values: 5, 8.0, "7". Print these variables, explain results###
a = int(5)
b = int(8.0)
c = int("7")

# Print the results
print(a)
print(b)
print(c)

# Explain the results: all values are converted to int

# -----------------------------------------------------------------------------------------------------------------------#

###Create string variable with value "Hello world". Print the string. Print length of the string.
# Print the first symbol of the string. Assign last 5 chars of the string to the new variable and print.
# Print all string in uppercase. Print the number of all "o" symbols in the string. Split string into two separate
# words and print each separately.

a = "Hello world"
print(a)
print(len(a))

first = a[0]
print(first)

b = a[-5:]  # if the string is long
c = a[6:11]  # if the string is short
print(b)
print(c)

print(str.upper(a))

o = a.count("o")
print(o)

split = a.split()
print(split)  # print the list with 2 separate words
print(split[0])  # print 1st word
print(split[1])  # print 2nd word

# -----------------------------------------------------------------------------------------------------------------------#

# Create two variables "name" and "age". Using string formatting print the next: "Hello my name is %name%, I`m %age%"
name = "Yana"
age = 30

# using old formatting using %
print("Hello my name is %s, I`m %d" % (name, age))

# using f-string
print(f"Hello my name is {name}, I`m {age}")

# using str.format
print("Hello my name is {}, I`m {}".format(name, age))

