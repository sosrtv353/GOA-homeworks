try:
    num=float(input("enter a number"))
    divided=float(input("enter another number for division"))
    print(num / divided)
except ZeroDivisionError:
    raise ZeroDivisionError("Cant divide with zero")
finally:
    print("operation complete")

# საკლასო დავალება:

# Write a function apply_to_list(func, values) that takes a function func and a list values, and returns a new list where func is applied to each element.

# Then:

# Define a function square(x) that returns the square of a number.
def square(x):
    return x**2

def apply_to_list(lister,func):
    return [func(x) for x in lister]

apply_to_list([1,2,3],square)