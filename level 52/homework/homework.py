def first_non_consecutive(arr):
    for i in range(1, len(arr)):     
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None

def to_alternating_case(string):
    if string.isupper():
        return string.lower()
    elif string.islower():
        return string.upper()
    return ''.join([x.lower() if x.isupper() else x.upper() for x in string])

def correct(s):
    final=""
    for i in s:
        if i == "5":
            final+="S"
        elif i == "0":
            final+="O"
        elif i == "1":
            final+="I"
        if i!= "5" and i!= "0" and  i!= "1":
            final+=i
        
    return final

def is_palindrome(s):
    return s[::-1].lower() == s.lower()

def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}" 
    return  f"${salary}"

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >=2:
        return 75
    return 0

def sum_str(a, b):  
    if a == "":
        a=0
    if b == "":
        b=0
    return str(int(a) + int(b))

def get_average(marks):
    return sum(marks) // len(marks)

def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"

def reverse_words(s):
    return " ".join(s.split(' ')[::-1])

def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]

def square(n):
    return n*n

def remove_every_other(my_list):
    new_list = []
    
    for i in range(len(my_list)):
        if i%2 == 0: new_list.append(my_list[i])
    
    return new_list

def remove_every_other(my_list):
    return my_list[::2]

def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)
    
    if res < 0: return res*-1
    return res

def str_count(strng, letter):
    return strng.count(letter)

def is_even(n): 
    return n % 2 == 0

def move(position, roll):
    return position + roll*2

def get_planet_name(id):
    planets=["nothing","Mercury","Venus","Earth","Mars","Jupiter","Saturn",'Uranus',"Neptune"]
    return planets[id]

def between(a,b):
    return list(range(a,b+1))

def is_uppercase(inp):
    return inp == inp.upper()

def monkey_count(n):
    return list(range(1, n+1))

        
