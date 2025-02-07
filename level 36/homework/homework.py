# code wars solutions:

def summation(num):
    saver=[]
    for i in range(num+1):
        saver.append(i)
    return sum(saver)
        
def find_smallest_int(arr):
    minimal=arr[0]
    for i in arr:
        if i < minimal:
            minimal=i
    return minimal
      
def string_to_number(s):
    return int(s)