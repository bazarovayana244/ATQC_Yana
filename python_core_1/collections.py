###Create a list with different types of data inside (str, int, float, boolean) and print###
list = ["The world is mine", 543, 6.9, False]
print(list)

# Print items from second to penultimate.
print(list[1:])

#Print number of items in list
print(len(list))

#Add new item to list and print - in the end
list.append(78.3)
print(list)

#Add new item on specific position and print
list.insert(3, "Hello world")
print(list)

#Change an item in the list and print
list[0] = "Enjoy the silence"
print(list)

#Replace two items with one new item and print - only for items in a row
list[3:5] = [True]
print(list)

#Remove item by value and print
list.remove(543)
print(list)

#Remove item by position and print
del list[1]
print(list)

#or use pop()
remove = list.pop(2)
print(remove) #can print the item that is deleted
print(list)


###Create two lists. Append one list with another, explain and print results.
# Expend one list with another, explain and print results###
list_a = ['Enjoy the silence', 6.9, True, 78.3]
list_b = ['The world is mine', 543, False]
print(list_a, list_b)

list_a.append(list_b)
print(list_a) #append add the 2nd list as one object to the 1st list

list_a.extend(list_b)
print(list_a) #extend add the items of the 2nd list to the 1st list


###Create dictionary with person info: name, surname, age - assign values###
dict = {"name": "John", "surname": "Doe", "age": 30}
print(dict)

#Print name and age
print(dict["name"], dict["age"])

#Print all keys of the dictionary
print(dict.keys())

#Print all values of the dictionary
print(dict.values())

#Change age and print name, surname, age
dict["age"] = 31
print(dict["name"], dict["surname"], dict["age"]) #print only values

#Add new item "maritalstatus" to the dictionary and print name and maritalstatus
dict["maritalstatus"] = "Married"
print(dict["name"], dict["maritalstatus"])

#Add new list item "children" to the dictionary with 3 names inside and print name and children
dict["children"] = ["Anna", "Jack", "Jill"]
print(dict["name"], dict["children"])

#Remove age from the dictionary and print all items
del dict["age"]
print(dict)


###Create the tuple with different data types (at least 10 items). Print all items###
tuple_a = (7, 5.78, 7 + 4j, 'Hello World', "Python", True, False, ["The world is mine", 543, 6.9, False],
           {"name": "John", "surname": "Doe", "age": 30}, {1, 2, 3})
print(tuple_a)

#Print last 4 items
print(tuple_a[-4:])
print(tuple_a[6:10])

#Return an index of tuple element by its value
print(tuple_a.index(False))

#Create another tuple, join both and print result
tuple_b = ( 67, 78.4, "It`s been avile", {"breed": "dachshund", "name": "Smoky"})
print(tuple_a + tuple_b)
#or create another tuple and then print
tuple_c = (tuple_a + tuple_b)
print(tuple_c)
#or use unpacking
print(*tuple_a, *tuple_b)

#Unpack tuple so the first 3 items unpacked to separate variables
#and rest of elements unpacked to one list element
a, b, c, *rest = tuple_a
print(a, b, c, rest) #print results in one line
print(a)
print(b)
print(c)
print(rest)