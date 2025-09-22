###Create function which will print "Hello world" when it is called###
def function():
    print("Hello world")
function()

# -----------------------------------------------------------------------------------------------------------------------#

###Create function which takes name and surname as parameters. Call this function with positional args.
# Call this function with keybord args###
def function(name, surname):
    print(f"Hello my name is {name} {surname}")

function("John", "Doe") #args

function(name="John", surname="Doe") #kwargs

# -----------------------------------------------------------------------------------------------------------------------#

#Create function that can be called by any number of args (dog breeds) and print "The first dog breed is %breed%"###
def dogs(*breed):
    print(f"The first dog breed is {breed[0]}")
dogs('dachshund', 'husky', 'beagle')

# -----------------------------------------------------------------------------------------------------------------------#

###Create a function which can be called with any number of arguments (name, surname, age). Print user`s name and age###
def person_data (**data):
    print(f"User`s name is {data["name"]} and age is {data["age"]}")
person_data(name = "John", surname = "Doe", age = 30)

# -----------------------------------------------------------------------------------------------------------------------#

###Create function print_person_info() which has name, surname, age and maritalstatus and print all this info.
#When calling function user is not required to specify age but can do so, when age is not provided it won`t be printed.
#MaritalStatus should print default value "unknown" if it is not defied when calling the function ###
def print_person_info(name, surname, age, maritalstatus):
    print(f"Name: {name}, Surname: {surname}, Age: {age}, Maritalstatus: {maritalstatus}")

#call function with age and maritalstatus specified
print_person_info("John", "Doe", 30, "Married")

#call function without age and maritalstatus specified
def print_person_info(name, surname, age=None, maritalstatus="unknown"):
    info = f"Name: {name}, Surname: {surname}"

    if age is not None:
        info += f", Age: {age}"

    info += f", Marital Status: {maritalstatus}"
    print(info)

print_person_info("John", "Doe", age=30, maritalstatus="Status")
print_person_info("Mary", "Smith")

# -----------------------------------------------------------------------------------------------------------------------#

#Using recursion write a function which will print factorial of the number which is passed
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_factorial(number):
    print(f"Factorial of {number} is {factorial(number)}")

print_factorial(9)

