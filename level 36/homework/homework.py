# code wars solutions:

def summation(num):
    saver=[]
    for i in range(num+1):
        saver.append(i)
    return sum(saver)
        
def make_upper_case(s):
    return s.upper()

def get_drink_by_profession(param):
    lowparam=param.lower()
    if lowparam == "jabroni":
        return "Patron Tequila"
    elif lowparam == "school counselor":
        return "Anything with Alcohol"
    elif lowparam == "programmer":
        return "Hipster Craft Beer"
    elif lowparam == "bike gang member":
        return "Moonshine"
    elif lowparam == "politician":
        return "Your tax dollars"
    elif lowparam == "rapper":
        return "Cristal"
    else: return "Beer"