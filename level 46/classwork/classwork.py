#საკლასო დავალება:

#შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

#თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

#ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით

def lister(start,end,step,user_num):
    saver=[x for x in range(start,end,step) if x > user_num]
    return saver

lister(1,21,2,30)


div=[i for i in range(1,100) if i % 3 == 0 or i % 5 == 0 ]
print(div)


palindroms=[p for p in range(10,201) if str(p)[::-1] == str(p)]