###Create two numeric variables x and y with different values. Perform addition, assign results to variable x and print###
x = 3
y = 8
x = x + y
print(x)

# -----------------------------------------------------------------------------------------------------------------------#

#Create int variable with value 10 and string variable with value "10". Divide both by 0. Explain and print the results
x = 10
y = "10"

#x_divide = x / 0 #can`t divide by 0 ZeroDvisionError
# y_divide = y / 0  #can`t divide str TypeError - should cast to int first
# y_int = int(y)
# y_divide = y_int / 0  #can`t divide by 0 ZeroDvisionError

# -----------------------------------------------------------------------------------------------------------------------#

#Using Casting create int, float, str with the same value and print.
#Compare them using comparison operators (>, <, ==, !=) and print results###
a = int(6)
b = float(6)
c = str(6)

print(a, b, c)

#Compare int and float
print(a > b)
print(a < b)
print(a == b)
print(a != b)

#Compare int or float with str - TypeError should cast str into int first

#Compare int with str converted to int
c_int = int(c)
print(a > c_int)
print(a < c_int)
print(a == c_int)
print(a != c_int)

# -----------------------------------------------------------------------------------------------------------------------#

###Create int variable x and assign it with 5 value. Using assignment operator += assign x with value 3.
#Print and explain result###
x = 5
x += 3
print(x) #the result is shortcut for addition x = 5 + 3 = 8

# -----------------------------------------------------------------------------------------------------------------------#

###Create two str variables "Tomato" and "Onion". Compare them using comparison operators and print results.
#Use arithmetic operator + and assign result to another variable###

x = "Tomato"
y = "Onion"
#Strings can be compared between themselves lexicographically (char by char)
print(x > y)
print(x < y)
print(x == y)
print(x != y)

xy = x + y #operator + works as concatenation on strings
print(xy)

# -----------------------------------------------------------------------------------------------------------------------#

