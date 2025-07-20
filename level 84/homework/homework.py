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




def reverse_letter(st):
    return "".join([c for c in st if c.isalpha()])[::-1]

def gimme(input_array):
    return input_array.index([i for i in input_array if i != min(input_array) and i != max(input_array)][0])

def angle(n):
    return (n - 2) * 180

def round_to_next5(n):
    counter = n
    while counter % 5 != 0:
        counter+=1
    return counter

def two_oldest_ages(ages):
    max_val = max(ages)
    lst = [max_val]
    ages[ages.index(max_val)] = 0
    lst.append(max(ages))
    lst.sort(reverse = False)
    return lst
    
    


