

names = ["Nika", "Dato", "Luka", "Vano", "Soso", "Rati"]

for i in range(len(names)): # 0, 1, 2, 3, 4, 5
    if i % 2 == 0:
        print(names[i])



numbers = [10, 20, 30, 40, 50]

numbers[3] = 100

print(numbers)



numbers = [10, 20, 30, 40, 50]

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if num1 > num2:
    print(numbers[num2: num1 + 1])
elif num2 > num1:
    print(numbers[num1: num2 + 1])
else:
    print([])

variable=[1,2,3,4,5,6,7,8,9,10,]
for u in variable:
    print(u)

var=[1,3,5,7,9,11]
print(var[0])
print(var[2])
print(var[5])

strr=["hello", "how are you", "im good too", "i have to go", "bye"]
print(strr[::-1 ])
# slicing არის ელემენტების ამოჭრა სიიდან და ასევე სლაისინგით შეგიძლია სიაში რომელიმე ელემენტებს შორის მოქცეული ელემენტებით ახალი 
# სიის გაკეთება.