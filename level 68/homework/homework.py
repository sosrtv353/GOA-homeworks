def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res

def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))

def high_and_low(numbers):
    nums = list(map(int, numbers.split(" ")))
    return f"{max(nums)} {min(nums)}"

def filter_list(l):
    return [i for i in l if type(i)!=str]

def descending_order(num):
    num_str = str(num)
    sorted_digits = sorted(num_str, reverse=True)
    sorted_str = ''.join(sorted_digits)
    return int(sorted_str)

import math
def is_square(n):    
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n
    
def get_middle(s):
    if len(s) % 2 == 0:
        return f"{s[(len(s) // 2) - 1]}{s[len(s) // 2]}" 
    return s[len(s) // 2]
    
def is_isogram(string):
    string = string.lower()  
    for s in string:
        if string.count(s) > 1:
            return False
    return True

def xo(s):
    s=s.lower()
    X = [x for x in s if x == "x"  ]
    O = [o for o in s if o == "o"]
    return len(X) == len(O)

def to_jaden_case(string):
    strings = string.split()
    return " ".join([x.capitalize() for x in strings])