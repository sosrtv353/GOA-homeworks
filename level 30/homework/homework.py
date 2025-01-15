# upper homeworks:
inp=str(input("Type anything:"))
print(inp.upper())
name= str(input("type your name:"))
print(name.upper())

def to_uppercase(input_string):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    result = ""
    for char in input_string:
        if char in lowercase:
            index = lowercase.index(char)
            result += uppercase[index]
        else:
            result += char 
            
    return result


input_string = input("Enter a string: ")
print("Uppercase version:", to_uppercase(input_string))

# end

# lower homeworks:
low=str(input("type anything"))
print(low.lower())
email=str(input("type your email address"))
email.lower()

def to_lower(inp_string):
    lowercase2 = 'abcdefghijklmnopqrstuvwxyz'
    uppercase2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    result = ""
    for char in input_string:
        if char in uppercase2:
            index = uppercase2.index(char)
            result += lowercase2[index]
        else:
            result += char 
            
    return result


input_string = input("Enter a string: ")
print("lowecase version:", to_uppercase(input_string))


# capitalize homeworks:
capitalized_input=str(input("type any string"))
capitalized_input.capitalize()

def manual_capitalize(c_str):
    if c_str[0].islower():
        c_str= c_str[0].upper()+ c_str[1:]
    print(c_str)
manual_capitalize("hello")
# end 
# find homeworks:
sentence= "a great programming language for beginners is python"
print(sentence.find("python"))
inp2=str(input("type anything"))
result=str(input("type any string to find its index "))
print(inp2.find(result))

def manual_finder(the_str, str_finder):
    saver=str(the_str)
    for char in range(len(the_str)):
        if saver[char]== str_finder:
            print(char)
    if saver[char] != str_finder:
        print("-1")
manual_finder("hello","o")
# end
# len homeworks:
users=str(input("type any string"))
print(len(users))

def manual_len(lstr):
    the_saver=0
    for char in lstr:
        the_saver+=1
    print(the_saver)
# end
# count homeworks:
sentence2="The Internet has become one of the most important resources in the world."
print(sentence2.count("the"))
inp3=str(input("type anything"))
occurence=str(input("type s occurence"))
print(inp3.count(occurence))

def manual_count(counter, counting):
    occurence2 = 0  
    index1 = len(counting)  
    for i in range(len(counter) - index1 + 1): 
        if counter[i:i + index1] == counting:
            occurence2 += 1 
    print(occurence2) 
# end
# index homeworks:
sentence3="hello there!"
print(sentence3.index("hello"))

def manual_index(_strr, str_finder_):
    saver2=str(_strr)
    for char in range(len(_strr)):
        if saver2[char]== str_finder_:
            print(char)
    if saver2[char]!= str_finder_:
        print(TypeError)
# end
# islower homeworks:
inp4=str(input("just type anything:"))
print(inp4.islower())

def manual_islower(unknown_str):
    if unknown_str == unknown_str.lower():
        return True
    else: return False


inp5=str(input("just type anything:"))
if inp5 == inp5.lower():
    print("its in lowercases")
else: print("its not in lowercase")
# end
# isupper homeworks:
inp6=str(input("just type anything:"))
if inp6 == inp6.upper():
    print("its in uppercase")
else: print("its in lowercase")

def manual_islower(unknown_str2):
    if unknown_str2 == unknown_str2.upper():
        return True
    else: return False

inp7=str(input("just type anything:"))
if inp7 == inp7.upper():
    print("its in uppercase")
else: print("its in lowercase")




