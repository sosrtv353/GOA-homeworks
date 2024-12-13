num1=int(input("enter number:"))
num2=int(input("enter number:"))
num3=int(input("enter number:"))
if num1>num2 and num1>num3:
    print(str(num1)+"is greater than these numbers")
elif num2>num1 and num2>num3:
    print(str(num2)+"is greater than these numbers")
else:
  print(str(num3)+"is greater than these numbers")  
    

grd=int(input("what is your score?"))
if grd >= 90 and grd <= 100:
   print("your grade is A")
elif grd >= 80 and grd < 90:
   print("your grade is B")
elif grd >= 70 and grd < 80:
   print("your grade is C")
elif grd >= 60 and grd < 70:
   print("your grade is D")
elif grd < 60:
   print("your grade is F")




number=int(input("enter number"))
if number>0:
   print("your number is positive")
elif number<0:
   print("your number is negative")
else:
   print("your number is zero")

# end

start = int(input("Please enter start number: "))
end = int(input("Please enter end number: "))

sum = 0

for i in range(start + 1, end):
    sum += i

print(sum)

number = int(input("Please enter a number: "))

# end

is_prime = True

for i in range(2, number // 2):
    if number % i == 0:
        is_prime = False
        break
        
if is_prime:
    print("The number is prime")
else:
    print("The numbers isn't prime")

# end

list0=[1,3,6,9,12,15]
list1=list0[0]
list2=list0[2]
list3=list0[5]

list5=["soso", 4, "6", True, 10, "hello", False, 2, "1", "greet", 5, 6, 9, "bye", 11, 13, "goodbye",8, 99, "finish"]
listt=list5[0]
listt1=list5[1]
listt2=list5[2]
listt3=list5[3]
listt4=list5[4]
listt5=list5[5]
listt6=list5[6]
listt7=list5[7]
listt8=list5[8]
listt9=list5[9]

listt10=list5[10]
listt11=list5[11]
listt12=list5[12]
listt13=list5[13]
listt14=list5[14]
listt15=list5[15]
listt16=list5[16]
listt17=list5[17]
listt18=list5[18]
listt19=list5[19]

# elif ვიყენებთ მაშინ როცა გვინდა რომ იგივე if ჩავაშენოთ პირობაში ისე რომ არ შეიცვალოს პირობა.
