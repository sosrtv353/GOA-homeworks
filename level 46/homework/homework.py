nums=[x for x in range(1,11)]
squared=[d ** 2 for d in range(1,6)]
even=[e for e in range(1,20) if e % 2 == 0]
words = ["Giorgi","Anna","Nino","Soso","Nika"]
first_letter=[l[0] for l in words]
upper_cased=[up.upper() for up in words]
div_by_three=[t for t in range(1,51) if t % 3 == 0]
extract=[ex[0:5] for ex in words]
celsiuses=[14,20,5,2]
faren=[c * (9/5) +32 for c in celsiuses]



prime_numbers = [i for i in range(2, 100) if len([x for x in range(2, int(i ** 0.5) + 1) if i % x == 0]) == 0]

print(prime_numbers)



words_list = [
    "Apple", "Banana", "Cat", "Dog", "Elephant", "Flame", "Galaxy", "Harmony",
    "Island", "Jungle", "Kite", "Lighthouse", "Mountain", "Nebula", "Ocean", 
    "Pineapple", "Quest", "Rainbow", "Sky", "Tree", "Unicorn", "Voyage", "Whale", 
    "Xylophone", "Yellow", "Zebra"
]

words = [i for i in words_list if len(i) > 5 and len([x for x in i.lower() if x in "aeiou"]) > 0]

print(words)



numbers = [0, 1]

number = [numbers.append(sum(numbers[-2:])) for _ in range(2, 20)]

print(numbers)