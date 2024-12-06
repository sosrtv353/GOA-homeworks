num1=int(input("enter number:"))
num2=int(input("enter number:"))
if num1>num2:
    print(str(num1) + "is greater than" + str(num2))
else:
    print(str(num2) + "is greater than" + str(num1))
# done
num=int(input("enter number:"))
if num%2==0:
    print("this number is even")
else:
    print("this number is odd")
# done
num11=int(input("enter number:"))
if num11<0:
    print ("this number is negative")
else:
    print("this number is positive")
# done
num5=int(input("enter number:"))
if num5%5==0:
    print("this number is divisible by 5")
else:
    print("this number isnt divisible by 5")
# done
for num in range(5):
    num=int(input("enter a number"))
    print(num)
    if num%2==0:
        print("even")
    else:
        print("odd")
#done
user_num=int(input('enter a number'))
user_num2=int(input("enter a second number for calculation"))
op=input("choose a operation method plus/minus/multiply/divide")
if op=="plus":
    print(user_num + user_num2)
if op=="minus":
    print(user_num-user_num2)
if op=="multiply":
    print(user_num/user_num2)
if op=="divide":
    print(user_num*user_num2)
# done
counter=0
password="GOA best"
while input("enter your password")!=password:
    print("your tried"+ str(counter)+"times")
    counter+=1
print("access granted")
print("your total tries:"+ str(counter))
# done

# if (ქართულად თუ) არის პირობითი განცხადება რითიც კომპიუტერს ვეუბნებით რომ როცა მოცემული კონდიციები ემთხვევა გაუშვას კოდი
#ხოლო თუ არა ვიყენებთ else რომელიც ალტერნატიურ კოდს უშვებს
