def row_weights(array):
    # team1 = even
    # team2 = odd
    team1 = []
    team2 = []
    for index,item in enumerate(array):
        if index % 2 == 0:
            team1.append(item)
        else: team2.append(item)
    return (sum(team1),sum(team2))


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    return int((sum([i * i for i in ages])**0.5)/2)


def greet(name): 
    return f"Hello {name.capitalize()}!"

def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))

def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return f"0=0"
    number = [i for i in range(n+1)]
    string_num = "+".join(str(i) for i in number)
    return f"{string_num} = {sum(number)}"

def even_numbers(arr,n):
    arr = [i for i in arr[::-1] if i%2==0]
    return arr[:n][::-1]

def sort_gift_code(code):
    return ''.join(sorted(code))

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr)[::-1]:
        return "yes, descending"
    return "no"

def remove_duplicate_words(s):
    seen = set()
    result = []
    for word in  s.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)

def words_to_marks(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for i in s:
        sum += alphabet.index(i) + 1 
    return sum

def largest_pair_sum(numbers): 
    numbers.sort()
    return numbers[-1] + numbers[-2]
