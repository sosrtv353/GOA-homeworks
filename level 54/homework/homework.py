try:
    num=float(input("Enter a number for division: "))
    num2=float(input("What number to divide by: "))
    print(f"Result: {num / num2}")
except ZeroDivisionError:
    print("You cant divide by zero")
except TypeError:
    print("You have to enter a number")
except ValueError:
    print("Enter a valid number")
finally:
    print("Operation complete")
try:
    food=["Burger","Pizza","Salad","Water","Mtswadi","Nataxtari","Khachapuri"]
    order=int(input(f"Which one do you want to order? enter a index {food}: "))
    print(f"Your order is: {food[order]}")
except IndexError:
    print("Enter a valid index")
except ValueError:
    print("Index has to be a number")
finally:
    print("I hope you enjoyed visiting us! :)")
    
try:
    dic1 = {
        "Name":"John",
        "Surname": "Johnson",
        "Age": 40,
        "Car": "Bmv",
        "Heigth": "180cm"

    }
    location=dic1["Location"]
except KeyError:
    print("Looks like this key dosent exist in the dictionary you are looking for")
finally:
    print("Searching complete ")

try: 
    converted=int(input("Enter a number for it to be converted into a integer: "))
    print(f"converted into a integer: {converted}")
except ValueError:
    print("You have to enter a number")
finally:
    print("Operation complete")
    

def greeter(name):
    return f"Hello {name}"
def greet(name,func):
    return func(name)
print(greet("soso",greeter))

def multiplier(num1,num2):
    return num1 * num2
def mult(number,number2,function):
    return function(number,number2)
print(mult(2,3,multiplier))