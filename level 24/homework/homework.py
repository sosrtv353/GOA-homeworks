li=["window", 6, False, "house", "bakery", 100, "street", 42, 55]
print(li[0])
print(li[-1])
print(li[0:3])
word="motorcycle"
print(word[5:10])
print(word[ ::-1 ])

li2=["one","two","three","four","five","six","seven","eight","nine","ten"]
for t in range(len(li2)):
    if t % 3 == 0:
        print(li2[t])


li3=[2,5,9,13,15,18,20,22]
middle=len(li3) // 2
first_halve=li3[: middle]
second_halve=li3[middle :]
print(first_halve)
print(second_halve)