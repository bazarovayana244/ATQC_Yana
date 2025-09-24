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
