def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)

def is_triangle(a, b, c):
    return a+b>c and c+b>a and c+a>b

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]

import math
def find_next_square(sq):
    if int(sq ** 0.5) ** 2 != sq:
        return -1
    return (math.isqrt(sq) + 1) * (math.isqrt(sq)+1)