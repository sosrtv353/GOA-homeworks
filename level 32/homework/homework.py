#format და f იგივე როლს ასრულებენ ოღონდ format დოტ ნოტაციით იწერება სიის ბოლოს ხოლო f იწერება ბრჭყალების უკან, (ანუ სინტაქსია განსხვავებული)
# append სიის ბოლოს ამატებს ელემენტს ხოლო insert-ით შეგვიძლია მივუთითოთ თუ რომელ ინდექსზე იყოს ეს ელემენტი
def name_surname(name,surname):
    print(f"hello there {name} {surname}")
inp=str(input("what is your name?:"))
inp2=str(input("whats your surname?:"))
name_surname(inp,inp2)

def fc(name2,surname2):
    name2=name2.capitalize()
    surname2=surname2.capitalize()
    print((f"{name2} {surname2}"))
fc("john","doe")
def reverese_f(string):
    string=string[::-1]
    print(f"formated: {string}")
reverese_f("hello world")

def inserter(sent, word, index):
    sent.insert(index,word)
    print(sent)
inserter(["hi","bye"],"goodnight",2)
def word_to_list(sentence):
    print(sentence.split())
word_to_list("apple melon strawberry")
def csv_list(csv):
    print(csv.split(","))
csv_list("python, java. c++")
def sentence_spliter(sentence3):
    print(sentence3.split("."))


def appender(item, app_list):
    app_list.append(item)

def returned_list(original_list, items):
    for i in items:
        original_list.append(i)
    print(original_list)
returned_list([],[True,"Hi",4])

def appending(list1,appender_list):
    for e in list1:
        appender_list.append(e)
appending([2,5,6],["table","chair",8,False])

def indexer(item2,list2,index2):
    list2.insert(index2,item2)

def beginning_insert(list3,item3):
    list3.insert(0,item3)

def end_insert(list4,item4):
    lened=len(list4)
    list4.insert(lened,item4)
    print(list4)
