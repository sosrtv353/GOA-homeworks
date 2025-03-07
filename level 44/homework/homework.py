def reverse_seq(n):
    final=[]
    for i in range(n,0,-1):
        final.append(i)
    return final
def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1  == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif  p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    else: return "Draw!"

def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0 

def count_sheep(n):
     return ''.join(f"{i} sheep..." for i in range(1, n + 1))

def get_grade(s1, s2, s3):
    if s1+s2+s3 >=270:
        return 'A'
    elif s1+s2+s3 >=240:
        return 'B'
    elif s1+s2+s3 >=210:
        return 'C'
    elif s1+s2+s3 >=180:
        return 'D'
    else: return 'F'


def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"

def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list

def find_average(numbers):
    if not numbers: return 0
    return sum(numbers) / len(numbers)

def smash(words):
    return " ".join(words)

def hero(bullets, dragons):
    return bullets >= dragons * 2

def count_positives_sum_negatives(arr):
    if arr == []:
        return []

    counter = 0
    sum_negative = 0
    for i in arr:
        if i > 0:
            counter += 1 
        elif i < 0:
            sum_negative += i
    result = [counter,sum_negative]
    if result != [0,0]:
        return result
    return [0,0]

def dna_to_rna(dna):
    return dna.replace("T", "U")

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    return False

def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)

    if your_points > other_avg: return True
    return False

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

def check(seq, elem):
    return elem in seq

def fake_bin(x): #creates fake binary system function
    final="" # variable to store things from cycle
    for i in x: # iterating over the parameter called x
        if int(i) < 5: 
            final+="0" # if int version of i is less than 5 then final variable stores a "0"
        else: final+="1" # else it stores 1
    return final # returns a variable that stores information

def count_by(x, n):
    result = []

    for i in range(1, n+1):
        result.append(x*i)

    return result