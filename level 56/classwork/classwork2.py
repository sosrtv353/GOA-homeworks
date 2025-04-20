def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res

def find_multiples(integer, limit):
    saved=[]
    for i in range(integer,limit+1):
        if i % integer == 0:
            saved.append(i)
    return saved