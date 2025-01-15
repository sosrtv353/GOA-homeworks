name=str(input("whats your name?"))
choice=str(input("l or u"))
if choice == "l":
    print(name.lower())
elif choice == "u":
     print(name.upper())
else: print("wrong information")


def manual_find(main_str, str_to_find):
    print(main_str.find(str_to_find))
manual_find("hello","h")

# # საკლასო დავალება:

# მომხმარებელს შემოატანინეთ მთავარი სთრინგი და შეინახეთ main_str ცვლადში.

# შემდეგ შემოატანინეთ დასათვლელი სთრინგი და შეინახეთ str_to_count ცვლადში.

# დაბეჭდეთ str_to_count რამდენჯერ შეგხვდება main_str ცვლადში
main_str=str(input("type anything"))
str_to_count=str(input("find any repeating strings:"))
print("the string is repeated",main_str.count(str_to_count),"times")

def manual_case(word):
    result=""
    for i in word:
        if i.islower():
            u= i.upper()
            result+=u
        elif i.isupper():
            l= i.lower()
            result+=l
    print(result)
manual_case("HHello")
