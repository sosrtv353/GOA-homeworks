# საკლასო დავალება:

# შექმენით dictionary, სადაც იქნება შემდეგი გასაღებები: name, surname, academy, fav-color, city, goa-student, age, fav-programming-lans
stats = {
    "name": "soso",
    "surname": "rtveliashvili",
    "academy": "GOA",
    "fav-color": "green",
    "goa student": True,
    "fav-programming-lang":"python"
}
print(stats["name"])
print(stats["surname"])
print(stats["academy"])
print(stats["fav-color"])
print(stats["goa student"])
print(stats["fav-programming-lang"])


for i in stats.keys():
    print(i)

for i in stats.values():
    print(i)

for i,s in stats.items():
    print(i,s)

for r,u in stats.items():
    print(f"{r} {u}")






