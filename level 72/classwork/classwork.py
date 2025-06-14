def find_short(s):
    s = s.split(" ")
    res = 1000000

    for i in s:
        if len(i) < res:
            res = len(i)
    return res

def solution(text, ending):
    return text.endswith(ending)

def accum(s):
    result = []
    for i in range(len(s)):
        letter = s[i]
        part = letter.upper()
        part += letter.lower() * i
        result.append(part)
    return '-'.join(result)

        
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])

def DNA_strand(dna):
    res = ""

    for base in dna:
        if base == "A": res+="T"
        elif base == "T": res+="A"
        elif base == "C": res+="G"
        else: res+="C"

    return res


def friend(x):
    return [f for f in x if len(f) == 4]

def add_binary(a,b):
    return bin(a+b)[2:]

def maskify(cc):
    if len(cc) <= 4:
        return cc
    return "".join(["#" if x < len(cc) - 4 else cc[x] for x in range(len(cc)) ])