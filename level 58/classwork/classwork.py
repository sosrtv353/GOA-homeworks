# საკლასო დავალება:

# შექმენით ანონიმური ფუნქცია, რომელსაც გადაეცემა სთრინგი. ფუნქციამ სთრინგი უნდა დააბრუნოს შემობრუნებული და შემდეგ capitalized ფორმატში გადაყვანილი. 

# ფუნქცია გამოიძახეთ 3-ჯერ, გადაეცით განსხვავებული არგუმენტები

reverse_capitalize=lambda string: string[::-1].capitalize()
print(reverse_capitalize("good"))
print(reverse_capitalize("hello"))
print(reverse_capitalize("python"))

print((lambda num: num*num)(4))


nums=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x ** 2, nums)))