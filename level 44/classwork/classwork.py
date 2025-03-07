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

def fake_bin(x):
    final=""
    for i in x:
        if int(i) < 5:
            final+="0"
        else: final+="1"
    return final

def count_by(x, n):
    result = []

    for i in range(1, n+1):
        result.append(x*i)

    return result