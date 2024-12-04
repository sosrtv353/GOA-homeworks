num=0
while num!=20:
    print(num)
    num+=2
for i in range(0,20,3) :
    print(i)

# საკლასო დავალება 3: 10-დან 30-ის ჩათვლით დაბეჭდეთ ყველა რიცხვი და თან მიუწერეთ ლუწია თუ კენტი
# , მაგ: 10 - even, 11 - odd, 12 - even და ასე გაგრძელდება 30-ის ჩათვლით
for w in range(10,30):
    if w%2==0:
        print("this number is even")
else:
    print("this number is odd")

# საკლასო დავალება: მომხმარებელს შემოატანინეთ 2 რიცხვი, num1, num2.

# თუ პირველი მეტია მეორეზე, შექმენით დიაპაზონი მეორე რიცხვიდან პირველი რიცხვის ჩათვლით და დაბეჭდეთ მხოლოდ ლუწი.

# ხოლო თუ მეორე რიცხვი მეტია პირველზე, შექმენით დიაპაზონი პირველიდან მეორეს ჩათვლით და დაბეჭდეთ მხოლოდ კენტი რიცხვები.

# საბოლოოდ დაბეჭდეთ ყველა ამ დაბეჭდილი რიცხვის ჯამი.

# num1=int(input("enter a number"))
# num2=int(input("enter a number"))
# if num1>num2:
#     for d in range(num2,num1):
#         d=d+2
# if num2>num1:
#         for k in range(num1,num2):
#          k+=2

num1, num2 = int(input("Enter your number: ")), int(input("Enter your number: "))

if num1 > num2:
    range1 = range(num2, num1 + 1)
    sum1 = 0

    # print only even numbers
    for i in range1:
        if i%2 == 0:
            print(i)
            sum1 += i
    
    print("Sum of all even numbers are:", str(sum1))
else:
    range2 = range(num1, num2 + 1)
    sum2 = 0

    # print only odd numbers
    for i in range2:
        if i%2 != 0:
            print(i)
            sum2 += i
    
    print("Sum of all even numbers are:", str(sum2))