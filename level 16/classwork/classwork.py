#num1=int(input("enter a number"))
#for u in range(0,num1):
   # print(u+num1)

password = "1234"

user_password = input("Enter a password: ")

while user_password != password:
    print("Incorrect password!")
    user_password = input("Enter a password: ")

print("Password is correct!")