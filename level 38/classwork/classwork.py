tuple1=("hello",5,"world",4.5,True,7,99,"goodbye","python",10)
for i in tuple1:
    print(i)

def no_duplicates(user_list):
    removed_d=list(set(user_list))
    print(removed_d)
    return removed_d
no_duplicates([1,1,1,2,3])
no_duplicates([5,6,7,10,10])
no_duplicates([5,5,5,5])