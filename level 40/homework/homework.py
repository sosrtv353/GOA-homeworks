def greet():
    return "Hello world!" # returns a "Hello World!"

def count_sheeps(sheep):
    return sheep.count(True) # counts True in a list of booleans

def no_space(x):
    return x.replace(" ", "") # replaces spaces with nothing (no spaces in a sentence)

def greet(name):
    return f"Hello, {name} how are you doing today?" # formated string

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2 # plus if operator is +
    elif operator == "-":
        return value1 - value2 # minus if operator is -
    elif operator == "*":
        return value1 * value2 # multiply if operator is *
    elif operator == "/":
        return value1 / value2 # divides if operator is /
    else: print("Invalid input") # if operator dosent match any of these match print this

def litres(time):
    return time // 2 # calculates how many you should drink in a hour (1 liter every 2 hour)

def century(year):
    century=0
    for i in range(0,year,100):
        century+=1 # for every 100 years a century += 1
    return century

def digitize(n):
    res_list = [] # saving list
    for i in str(n)[::-1]: # reversed and string version of n
        res_list.append(int(i)) # makes it integer for appending

    return res_list

def maps(a):
    saver=[] # saver variable for saving
    for i in a:
        saver.append(i*2) # every number is doubled
    return saver

# ამოცანები:
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

def make_upper_case(s):
    return s.upper()

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name+" plays banjo"
    else: return name+" does not play banjo"

def abbrev_name(name):
    words = name.split()
    first = words[0][0].upper()
    second  = words[1][0].upper()
    return first + "." + second

def past(h, m, s):
    return(s + m * 60 + h * 3600)*1000