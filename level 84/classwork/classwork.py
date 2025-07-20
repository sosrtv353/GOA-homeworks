def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number + 1,step))

def sort_by_length(arr):
    return sorted(arr, key=lambda x: len(x))

def nb_dig(n, d):
    count = 0
    for k in range(n + 1):
        squareStr = str(k * k)
        count += squareStr.count(str(d))
    return count

def remove_url_anchor(url):
    return url.split("#")[0]

def dont_give_me_five(start,end):
    res = 0
    for i in range(start,end + 1):
        if "5" not in str(i):
            res+=1
    return res
        
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def sum_digits(number):
    number = [int(i) for i in str(number) if i in "0123456789"]
    return sum(number)

