###Try to find out and fix the errors in debug mode (using breakpoints, evaluate)###
#TASK 1#
def favorite_ice_cream():
    ice_creams = [
        'chocolate',
        'vanilla',
        'strawberry'
    ]
    print(ice_creams[2]) #there is no [3] index, the last one is [2]
favorite_ice_cream()

#TASK 2#
def some_function(): # ":" is needed
    msg = 'hello, world!'
    print(msg)
    return msg # no spaces before "return"

#TASK 3#
file_handle = open('myfile.txt', 'r') #can`t use 'w' for reading file
file_handle.read()

#TASK 4#
def print_message(day):
    messages = {
        'monday': 'Hello, world!',
        'tuesday': 'Today is Tuesday!',
        'wednesday': 'It is the middle of the week.',
        'thursday': 'Today is Donnerstag in German!',
        'friday': 'Last day of the week!',
        'saturday': 'Hooray for the weekend!',
        'sunday': 'Aw, the weekend is almost over.'
    }
    print(messages[day])
def print_friday_message():
    print_message('friday') #the key 'friday' is in lowercase in the dictionary, so we should use the same key in the function
print_friday_message()

#TASK 5#
file_handle = open('myfile.txt', 'r') #there is no errors, but 'myfile.txt' should exist
