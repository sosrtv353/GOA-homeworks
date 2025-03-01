# მტავარი განსხვავება დიქთში და სხვა კოლექციის ტიპებში არის სტრუქტურა. dict ინახავს მნიშვნელობას გასაღებებში (key)
# key არის მნიშვნელობის შემნახავი. ის ყოველთვის უნდა იყოს სტრინგის სახით (თორე ისე ცუდი მიდგომაა). გასაღებები თითქმის იგივეა რაც ცვლადი
# value არის რომელიმე მონაცემთა ტიპი შენახული გასაღებებში
dict1 = {
    "name": "john",
    "surname": "doe",
    "age": 25,
    "fav-color": "black"
}

print(dict1.keys())
print(dict1.values())
print(dict1.items())
for key,value in dict1.items():
    print(f"{key} : {value}")

if "age" in dict1:
    print("age is in the dictionary")
else: print("the key age isnt in the dictionary")

gotten_key=dict1.get("name", "key not found")
print(gotten_key)
dict1.update({"heigth":"178cm"})
print(dict1)
dict1.pop("fav-color")
print(dict1)
print(len(dict1))
def sum_of_values(numbers):
    return (sum(numbers.values()))
sum_of_values( {
    "nss":1,
    "srs":5

})
dict1.clear()
print(dict1)

my_info = {
    "my_name":"Soso",
    "my_surname": "Rtveliashvili",
    "my_age": 14,
    "my_fav_color": "Green",
    "fav-programming language": "Python And C#",
    "studying_in_Goa": True,
    "heigth": "178cm",
    "hobbies": ["Basketball","Programming"],
    "fav_number": 3,
    "birthday": "August 21"
}