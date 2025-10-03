def min_value(digits):
    number = []
    digits = list(set(digits))  # Remove duplicates
    while digits:
        smallest = min(digits)
        number.append(smallest)
        digits.remove(smallest)
    return int(''.join(map(str, number)))


def triangular(n):
    if n <= 0:
        return 0
    return n * (n + 1) // 2

def sum_of_minimums(numbers):
    save =[]
    for i in numbers:
        save.append(min(i))
    return sum(save)

def fizzbuzz(n):
    l = []
    
    for i in range(1,n + 1):
        if i % 3 ==0 and i % 5 == 0:
            l.append("FizzBuzz")       
        elif i % 3 ==0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        else:
            l.append(i)
    return l
            

        