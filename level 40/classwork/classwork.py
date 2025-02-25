# codewars:
def greet():
    return "Hello world!" 

def count_sheeps(sheep):
    return sheep.count(True) 

def no_space(x):
    return x.replace(" ", "") 

def greet(name):
    return f"Hello, {name} how are you doing today?"

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2 
    elif operator == "-":
        return value1 - value2 
    elif operator == "*":
        return value1 * value2 
    else:
        return value1 / value2

def litres(time):
    return time // 2

def century(year): 
    return (year + 99) // 100

def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]

    res_list = []

    for i in reversed_str:
        res_list.append(int(i))

    return res_list

def maps(a):
    saver=[]
    for i in a:
        saver.append(i*2)
    return saver

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0:
        return True
    else:
        return False
def lovefunc2( flower3, flower4 ):
    return (flower3 + flower4)%2 == 1

def sum_array(a):
    return sum(a)
    
def lovefunc2( flower3, flower4 ):
    return (flower3 + flower4)%2 == 1

def sum_array(a):
    return sum(a)
    