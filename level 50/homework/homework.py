try:
    user_num=int(input("Enter a number:"))
    print("Thanks for typing a number")
except:
    print("you should have typed in a number")

try:
    listed=["Sleep",4.5,True,"Wake up","study"]
    index=listed[5]
except IndexError:
    print("Index out of range")

try:
    age=int(input("Whats your age?"))
    print(f"Hello, your age is:"+age)
except TypeError:
    print("There is a typeError in the code")
