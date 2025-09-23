###Use "try..except..finally" to process the exceptions. Check Exception Hierarchy.  Create a numeric variable.
# Divide it by zero. Handle exception and print in console exception message###
try:
    print(x)
except ZeroDivisionError:
    print("Zero division error")
except ArithmeticError:
    print("Arithmetic error")
except Exception:
    print("General error")
#x = 5/0 - raises Zero division error
#x = math.exp(1000) - raises Arithmetic error"

x = 10
try:
    result = 10 / 0
except:
    print("An error occurred: you can`t divide by zero")

###Create custom exception and raise it###
x = -10
try:
    if x < 0:
        raise Exception("No negative values")
except Exception as e:
    print("Custom exception:", e)
finally:
    print("Custom exception is raised")

###Try to find out and fix the errors in debug mode (using breakpoints, evaluate)###
#TASK 1#
def favorite_ice_cream():
    ice_creams = [
        'chocolate',
        'vanilla',
        'strawberry'
    ]
    print(ice_creams[3])
^
favorite_ice_cream()


#TASK 2#
def some_function()
    msg = 'hello, world!'
    print(msg)
     return msg

#TASK 3#
file_handle = open('myfile.txt', 'w')
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
    print_message('Friday')

print_friday_message()

#TASK 5#
file_handle = open('myfile.txt', 'r')
