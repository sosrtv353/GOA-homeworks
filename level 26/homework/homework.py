def manual_max(numbers):
    max_number = 0
    for i in numbers:
        if i > max_number:
            max_number = i
    print(max_number)

manual_max([5,7,8,10,15])




def calculate(num1, num2, operator):
    if operator== "+":
        print(num1 + num2)
    elif operator== "-":
        print(num1 - num2)
    elif operator== "*":
        print(num1 * num2)
    elif operator== "/":
        print(num1 / num2)
calculate(3, 5, "+")


def factorial(number):    
    factorial=1
    for i in range(number-1):
        number=number * factorial
        factorial+=1
    print(number)
factorial(5)

def num_checker(num):
    if num % 2 == 0:
        print("this number is even")
    elif num % 2 != 0:
        print("this number is odd")
    elif num == 0:
        print("your number is zero")
    else:
        print("your nnumber is negative")
num_checker(5)

def reverse(word):
    reversed=word[::-1]
    print(reversed)
reverse("hello")