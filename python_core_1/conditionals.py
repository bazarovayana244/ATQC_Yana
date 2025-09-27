###Create two int variables with different values. Write a condition, which prints "Yes, this is True",
#if 1st variable is bigger than 2nd###
a = 45
b = 36
if a > b:
    print("Yes, this is True")
#Change the values
a = 24
b = 569
if a > b:
    print ("Yes, this is True")
#the boolean expression is false, so anything is printed


#Create two int variables with different values. Write a condition, which prints "x is bigger than y",
# prints "x is equal to y", or prints "y is bigger than x"
x = 34
y = 67
if x > y:
    print("x is bigger than y")
elif x == y:
    print("x is equal to y")
else:
    print("y is bigger than x")
#Change variables to get another result
x = 785
y = 24
if x > y:
    print("x is bigger than y")
elif x == y:
    print("x is equal to y")
else:
    print("y is bigger than x")
#Change variables to get another result
x = 6
y = 6
if x > y:
    print("x is bigger than y")
elif x == y:
    print("x is equal to y")
else:
    print("y is bigger than x")


###Create str variable with value "The world is mine". Create condition which prints "Yes, this is true",
# if str contains word "mine", else prints "No, it`s not"###

x = "The world is mine"
if "mine" in x:
    print("Yes, this is true")
else:
    print("No, it`s not")
#Change the str to get another result
x = "The world is yours"
if "mine" in x:
    print("Yes, this is true")
else:
    print("No, it`s not")
