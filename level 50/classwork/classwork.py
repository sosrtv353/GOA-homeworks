# 1)შექმენი ცვლადი სადაც შეინახავ ინტეჯერს , შემდეგ გააკეთეთ TypeError, გაუშვით მისი შესაბამისი კოდი, გააკეთეთ try, except ბლოკები


# 2)მომხმარებელს შემოატანინეთ რაღაც მონაცემი (მაგ:სახელი ან გვარი)
#  და try,except ბლოკების საშუალებით გააკონტროლეთ ყველა ერორის შემთხვევა რაც არსებობს


num=5
try:
    print("hello" - num)
except TypeError:
    print("Theres a error in this code")

name=input("whats your name?")
try:
    print(name[0])
    if name.isdigit():
        print(name - 2)
except:
    print("Invalid data type")