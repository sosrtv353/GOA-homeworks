# საკლასო დავალება:

# შექმენით ფუნქცია სახელად generate_big_sentence, რომელსაც გადაეცემა 3 პარამეტრი - name, surname, age.

# ფუნქციამ უნდა გამოგვიტანოს წინადადება ზუსტად იგივე წყობით, როგორც მე დავწერე (გადახედეთ რესურებს), გამოიყენეთ format ფუნქცია.

# სანამ ფუნქციას გამოიძახებთ, მომხმარებელს შემოატანინეთ ტერმინალიდან სახელი, გვარი, ასაკი და შეინახეთ ისინი ცვლადებში.

# ფუნქციის გამოძახებისას, მას არგუმენტებად უნდა გადაეცეს ეს ცვლადები
name=str(input("whats your name"))
surname=str(input("whats your last name"))
age=str(input("whats your age"))


def generate_big_sentence(name, surname, age):
    print("hello {},{}, as we know your age is {},".format(name,surname,age))




name="soso"
surname="rtveliashvili"
age="14"
print(f"hello my name is {name} and my surname is {surname} my age is {age}")
# საკლასო დავალება:

# დ my_split, რომელსაც გადაეცემა ორი პარამეტრი - main_string და string_to_split.

# ფუნქციამ უნდა დაბეჭდოს სია - main_string გაიხლიჩოს string_to_split-ის მიხედვით.

# ფუნქციის გამოძახებამდე მომხარებელს შემოატანინეთ მთავარი და დასაყოფი სთრინგები, შეინახეთ ცვლადებში. შემდეგ გამოიძახეთ ფუნქცია და ეს ცვლადები გადაეცით არგუმენტებად# შექმენით ფუნქცია სახელა
def my_split(main_string, string_to_split):
    main_string.split(string_to_split)
userinp1=str(input("type any string"))
userinp2=str(input("now how do you want to split them?"))
my_split(userinp1,userinp2)

# საკლასო დავალება:

# შექმენით ფუნქცია სახელად manual_append. ამ ფუნქციამ სიის ბოლოში უნდა ჩაამატოს ახალი ელემენტი.

# არ გამოიყენოთ append, გამოიყენეთ insert.

# ფუნქციას ექნება 2 პარამეტრი - main_list, item_to_insert.
def manual_append(main_list, item_to_insert):
    the_len=len(main_list)-1
    main_list[len(main_list)]=item_to_insert
manual_append(["hi","hello","world"],"bye")