###Create list ['orange', 'apple', 'banana', 'cherry']. Print all items in the list using for loop###
fruits = ["orange", "apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Print item if it`s apple
for x in fruits:
    if x == "apple":
        print(x)

#Print all items and their length next to them
for x in fruits:
    print(x, len(x))


#Using for loop print all the numbers in range from 2 to 99 including
for x in range(2, 100):
    print(x)


#Using while loop print all the numbers 16<
x = 0
while x < 16:
    print(x)
    x += 1 #using counter


#Using while loop print all numbers in range from 3 to 33 including
x = 3
while x <= 33:
    print(x)
    x += 1


###Create list ["orange", "apple", "banana", "cherry"]. Create a function that will iterate and print the items
# and break from the function, when it reaches "banana".###
list = ["orange", "apple", "banana", "cherry"]
def print_until_banana (items, stop_item):
    for item in items:
        if item == stop_item:
            break
        print(item)
print_until_banana(list, "banana")

#Create a function that will iterate and print all items except "banana"
def print_except_banana (items, exclude):
    for item in items:
        if item == exclude:
            continue
        print(item)
print_except_banana(list, "banana")