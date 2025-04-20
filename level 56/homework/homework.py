
def fullname(name,surname):
    print(f"Hello {name} {surname}")
fullname("Ioseb","Rtveliashvili") #function that prints name and surname

print("Your maximum is someones minimum")

print("Violets are blue")
print("Roses are red")
print("Python is the best")

print(f"5 + 5 = {5+5}")

print("*")
print("**")
print("***")
print("****")
print("*****")

str_num="12"
int_num=int(str_num) #converting to integer
print(int_num)#printing result

flt=7.2
flt2=4.5
print(flt + flt2)

greet="hello"
proffesion="coder"
print(greet+" "+ proffesion) #concatinates 2 strings

B=True
print(type(B)) #checks type of the variable
try:
    age=int(input("Whats your age?: ")) #asks the age
    print(f"you will be {age + 1} next year") #prints age + 1
except:
    print("Stop joking around")

def greeter(name):
    print(f"Hello {name}") #functon that prints the name


nums=[float(input("Enter number: ")), float(input("Another number please: "))] #2 inputs in a list
print(sum(nums)) #sum of the list

color=input("Whats your favorite color?: ") #asks user favorite color
print(f"Your favorite color is: {color}")  #prints users favorite color

heigth=int((input("whats your heigth? (in cms): "))) #asks user heigth
if heigth<= 150:
    print("You are short") #prints if shorter than or equal to 150
elif heigth >= 170 and heigth <= 179:
    print("Average heigth") #same logic with diff numbers
else: print("You are tall") #if none of the conditions true it will print this

for i in range(1,6): #starts loop
    print(i) #prints numbers

for i in "Loop": #this loop writes letters on diff lines
    print(i) 

sums=[]
for i in range(1,11): #starts loop
    sums.append(i) #appends numbers to a list
print(sum(sums))

for i in range(1,11): #makes a loop in which it prints multiplication table of each number
    print(f"{str(i)} * 1")
    print(f"{str(i)} * 2")
    print(f"{str(i)} * 3")
    print(f"{str(i)} * 4")
    print(f"{str(i)} * 5")
    print(f"{str(i)} * 6")
    print(f"{str(i)} * 7")
    print(f"{str(i)} * 8")
    print(f"{str(i)} * 9")
    print(f"{str(i)} * 10")

for e in range(2,21):
    if e % 2 == 0:
        print(e) #prints num if e % 2 is 0
    
stop=1
while stop < 5: #using while loop for cycle
    print(stop)
    stop+=1

cycler=1
lst=[]
while cycler < 5: #using while loop for cycle
    lst.append(cycler)
    cycler+=1

nummer = 1  
total = 0  
while nummer <= 5:
    total += nummer  # add current number to total
    nummer += 1  # go to next number
print(total)

count = 10
while count >= 1:
    print(count)
    count -= 1  # decreasing the number each time

odd = 1
while odd <= 10:
    if odd % 2 != 0:
        print(odd)  # only prints if number is odd
    odd += 1

text = ""
while text != "exit":
    text = input("Say something (type 'exit' to stop): ") 
    if text != "exit": #if text isnt exit then continiue on with the loop
        print(f"You said: {text}")  


items = ["apple", "banana", "cherry"]
i = 0
while i < len(items):
    print(items[i])  # prints item at current index
    i += 1

my_list = [2, 4, 6, 8, 10]
print(f"List length: {len(my_list)}")  # len() is used for calculating list length

nums = [100, 200, 300, 400]
print(f"Second element: {nums[1]}")  # index 1 means second item

colors = ["red", "blue", "green"]
colors.append("yellow")  # adds "yellow" to the end of list
print(colors)


fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  # removes 'banana' from the list
print(fruits)

squares = [x**2 for x in range(1, 6)]  # ** squares the number so 2**2 = 4
print(squares)

evens = [x for x in range(2, 11) if x % 2 == 0]  # using list comprehension for even numbers
print(evens)

nums = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in nums if x % 2 != 0]  # keeps only odd numbers
print(odds)

words = ["hello", "world", "python"]
uppercased = [word.upper() for word in words]  # upper func makes text uppercase
print(uppercased)

nums = [1, 2, 3, 4, 5, 6]
even_squares = [x**2 for x in nums if x % 2 == 0]  # square only even numbers
print(even_squares)


def greet(name):  # takes a name as a parameter
    print(f"Hello, {name}!")  # prints greeting
greet("Ioseb")


def add(a, b):
    return a + b  # returns the sum

print(add(3, 5))


def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"  # checks if number is even or odd

print(even_or_odd(7))


def rectangle_area(length, width):
    return length * width  # area formula

print(rectangle_area(5, 3))

def reverse_string(s):
    return s[::-1]  # slicing to reverse

print(reverse_string("python"))

my_tuple = (42, "hello", 3.14)  # tuple with diff types
print(my_tuple)

t = ("a", "b", "c", "d")
print(t[1])  # slicing works same as a list


info = (1, 2, 3, 4, 5)
print(len(info)) # using len

tup1=(1,5,9)
tup2=("House","Book",False,5.5)
print(tup1+tup2)

tupl=(5,"Window","Carrot",3.14)
if 3.14 in tupl:
    print("Found")
else: print("Not Found")

# 47) Create and print a set
my_set = {1, 2, 3}  # set with 3 numbers
print(my_set)

# 48) Check if an element is in a set
check_set = {"apple", "banana", "cherry"}
if "banana" in check_set:  # checks if 'banana' exists
    print("Yes")
else:
    print("No")


nums = {10, 20, 30}
nums.add(40)  # adds 40 to the set
print(nums)


colors = {"red", "green", "blue"}
colors.remove("green")  # removes 'green'
print(colors)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # combines both sets
print(union_set)

me = {"name": "Ioseb", "age": 22}  # dictionary with two keys
print(me)

print(me["name"])  # gets the key


me["job"] = "coder"  # adds a new key called 'job'
print(me)

a = "code"
b = "wa.rs"
name = a + b

def get_char(c):
    return chr(c)

def expression_matter(a, b, c):
    combs = [
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c),
        a + (b * c),
        (a * b) + c
    ]
    return max(combs)
def how_much_i_love_you(nb_petals):
    num=nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"

def reverse_list(l):
    return l[::-1]

def odd_count(n):
    return n//2

def find_difference(a, b):
    v_a = a[0] * a[1] * a[2]
    v_b = b[0] * b[1] * b[2]
    
    if v_a > v_b: return v_a - v_b
    return v_b - v_a

def greet(language):
    all_lang = [ 
        ("english", "Welcome")
        , ("czech", "Vitejte")
        , ("danish", "Velkomst")
        , ("dutch", "Welkom")
        , ("estonian", "Tere tulemast")
        , ("finnish", "Tervetuloa")
        , ("flemish", "Welgekomen")
        , ("french", "Bienvenue")
        , ("german", "Willkommen")
        , ("irish", "Failte")
        , ("italian", "Benvenuto")
        , ("latvian", "Gaidits")
        , ("lithuanian", "Laukiamas")
        , ("polish", "Witamy")
        , ("spanish", "Bienvenido")
        , ("swedish", "Valkommen")
        , ("welsh", "Croeso")
    ]
    
    for key in all_lang:
        if key[0] == language: return key[1]
    
    return "Welcome"

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

def solution(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a
    
def fix_the_meerkat(arr):
    arr.reverse()
    return arr












