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
    planets=["nn","Mercury","Venus","Earth","Mars","Jupiter","Saturn",'Uranus',"Neptune"]
    return planets[id]

def between(a,b):
    return list(range(a, b+1))

def is_uppercase(inp):
    return inp == inp.upper()

def monkey_count(n):
    return list(range(1, n+1))

        
