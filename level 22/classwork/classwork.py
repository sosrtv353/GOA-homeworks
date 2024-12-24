li=[5,8,"apple",True,10,20,4.5,"pear",False,"grape"]
user=int(input("enter a number:"))
if user>=0 and user<len(li):
    print(li[user])
elif user>=len(li)*1 and user <=1:
    print(li[user])
else:
    print(None)



list1=[2,4,6,8,10,12,14,16,18,20]
for i in list1:
    print(i*2)
    print(i/2)