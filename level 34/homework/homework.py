def greet():
    print("Hello World!")

def summ(number1, number2):
    print(number1+number2)

def multiplier():
    inputer= float(input("type any number to multiply it by 10:"))
    print(inputer / 10)
    return inputer / 10
multiplier()

def welcomer(name="guest"):
    print(f"Hello {name}")

def usg(num1,num2):
    saver=[]
    usg=[]
    for i in range(num1+1):
        if num1 % i == 0:
            saver.append(i)
    for n in range(num2+1):
        if num2 % n == 0:
            saver.append(n)
        
        def another_usg():
            for e in saver:
                if num1 % e == 0 and num2 % e == 0:
                    e.append(usg)
                    return usg
def even_odd(numbers):
    for d in numbers:
        if d % 2 == 0:
            print("even")
        else: print("odd")

def maximum(numbers2):
    saver=numbers2[0]
    for num in numbers2:
        if num > saver:
            saver=num
    return saver 
# or you can just use the max() function

def positives(list_nums):
    positives=[]
    for pn in list_nums:
        if pn >= 0:
            positives.append(pn)
    return positives

def div_by_three(up_to):
    divided=[]
    for divs in range(0,up_to,3):
        divided.append(divs)
    if up_to < 3:
        print("type a number that is higher than 3")
        return None    #it will be a error if max() is used on a empty list
    return max(divided)
    
                    




    


