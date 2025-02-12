tapli=("honey",7.99,"orange","yellow",10)
price=tapli[1]
rating=tapli[4]
variety=tapli[1:4]
info=("John","Johnson",30,"car","house")
name,surname,age,*properties=info
print(name)
print(surname)
print(age)
print(properties)
random_nums=(1,1,2,2,3,4,5)
c=random_nums.count(1)
print(c)
i=random_nums.index(2)
print(i)

set_of_data={"string",5,1.2,True,False}
set_of_data.add("second string")
set_of_data.remove(False)
print(set_of_data)
if 1.2 in set_of_data:
    print("it is in this set")
else: print("its not")

nums={1,2,3,4,5}
nums2={6,7,8,9,10}
print(nums.union(nums2))

nums3={5,6,7,9}
nums4={5,7,8}
print(nums3.intersection(nums4))

print(nums3.difference(nums4))
listed=["walk","study","sleep","rest"]
print(list(set(listed)))
