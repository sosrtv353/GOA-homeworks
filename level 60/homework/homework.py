def mouth_size(animal):
    if animal.lower() == 'alligator':
        return 'small'
    else:
        return 'wide'

def nth_even(n):
    return (n - 1) * 2

def replace_exclamation(st):
    return ''.join(['!' if x in 'aeiouAEIOU' else x for x in st])

def unusual_five():
    return ["s","o","s","o","r","w"].index("w") 

def add_length(str_):
    return [f"{x} {len(x)}" for x in str_.split()]