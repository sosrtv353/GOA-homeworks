def reverse_letter(st):
    filtered_st = ""

    for i in st:
        if i.isalpha():
            filtered_st += i

    return filtered_st[::-1]


def gimme(input_array):
    # input_array = [10, 5, 2]

    sorted_arr = sorted(input_array)
    # sorted_arr = [2, 5, 10]

    mid_l = sorted_arr[1]
    # mid_l = 5

    return input_array.index(mid_l)
    # [10, 5, 2].index(5) = 1

def angle(n):
    return (n-2)*180

def round_to_next5(n):
    if n%5 == 0: return n

    return (n//5 + 1) * 5

def two_oldest_ages(ages):
    ages = sorted(ages)

    return [ages[-2], ages[-1]]


def capitalize(s):
    even = [s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))  ]
    odd = [s[i].upper() if i % 2 != 0 else s[i] for i in range(len(s))  ]
    return ["".join(even),"".join(odd)]


def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0
        elif arr2[i] == arr1[i]:
            score += 4
        else: score-= 1
    if score < 0:
        return 0
    return score

def solve(s):
    lowercase = 0
    uppercase = 0
    for i in s:
        if i.islower():
            lowercase+=1
        elif i.isupper():
            uppercase+=1
    if lowercase == uppercase:
        return s.lower()
    elif lowercase > uppercase:
        return s.lower()
    else: return s.upper()