def check_coupon(entered_code, correct_code, current_date, expiration_date):
    dates = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    current_date = current_date.split()
    expiration_date = expiration_date.split()

    if entered_code != str(correct_code):
        return False

    if int(current_date[2]) < int(expiration_date[2]):
        return True
    elif int(current_date[2]) > int(expiration_date[2]):
        return False
    elif dates[current_date[0]] < dates[expiration_date[0]]:
        return True
    elif dates[current_date[0]] > dates[expiration_date[0]]:
        return False
    else:
        if int(current_date[1][:-1]) <= int(expiration_date[1][:-1]):
            return True
        else:
            return False


def in_asc_order(arr):
    return arr == sorted(arr)

def flatten_and_sort(array):
    return sorted([i for lst in array for i in lst])

def factorial(n):
    fact = 1
    for i in range(1,n + 1):
        fact *= i
    return fact
    
def mxdiflg(a1, a2):
    
    if a1 == [] or a2 == []:
        return -1
    
    len1 = []
    len2 = []
    
    for i in a1:
        len1.append(len(i))
        
    for i in a2:
        len2.append(len(i))
        
    l = []
    for i in len1:
        for x in len2:
            l.append(abs(i - x))
            
    return max(l)