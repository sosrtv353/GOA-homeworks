def greet(name, owner):
    if name == owner:
        return "Hello boss"
    return "Hello guest"

def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        cost  -= 50
    elif d >= 3 and d < 7:
        cost -=20
    return cost

def quarter_of(month):
    if month < 4: return 1
    elif month < 7: return 2
    elif month < 10: return 3
    return 4

def remove_exclamation_marks(s):
    return s.replace("!","")

def points(games):
    total_points = 0

    for game in games:
        x = game[0]
        y = game[2]

        if x > y: total_points += 3
        elif x == y: total_points += 1

    return total_points

def get_volume_of_cuboid(length, width, height):
    return length*width*height

def area_or_perimeter(l , w):
    if l == w:
        return l*w
    return 2 (l + w)

def update_light(current):
    if current == "green": return "yellow"
    elif current == "yellow":  return "red"
    return "green"

def other_angle(a, b):
    whole = 180
    Total = a+b
    return whole - Total

def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    return False

def sum_mix(arr):
    return sum([int(i) for i in arr])

def sum_array(arr):
    if arr is None or len(arr) == 1 or len(arr) == 0: return 0

    min_ind = arr.index(min(arr))
    arr.pop(min_ind)

    max_ind = arr.index(max(arr))
    arr.pop(max_ind)

    return sum(arr)