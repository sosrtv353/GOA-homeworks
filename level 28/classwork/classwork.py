# საკლასო დავალება: შექმენით ფუნქცია სახელად manual_index, რომელსაც ექნება 2 პარამეტრი - მთავარი სთრინგი და საძიებელი სთრინგი.

# თქვენი დავალებაა რომ დააბრუნოთ მთავარ სთრინგში საძიებელი სთრინგი მერამდენე ინდექსზეა



def manual_index(strr, searchstr):
    checker=strr.index(searchstr)
    while searchstr[0:]!=checker:
        searchstr+=1
    print(checker)
    

manual_index("hello", "o")