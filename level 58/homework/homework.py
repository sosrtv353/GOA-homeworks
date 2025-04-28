add_five = lambda x: x + 5
multiply = lambda x, y: x * y
is_even = lambda x: x % 2 == 0
c_to_f = lambda temps: list(map(lambda c: (c * 9/5) + 32, temps))
starts_with_a = lambda s: s.startswith('A')

list(map(lambda x: x + 10, [1, 2, 3, 4, 5]))
list(map(lambda s: s.upper(), ["apple", "banana", "cherry"]))
list(map(lambda word: len(word), ["hello", "world", "python"]))
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
list(map(lambda x: str(x), [1, 2, 3, 4, 5]))
list(map(lambda name: "Hello " + name, ["Alice", "Bob", "Charlie"]))
list(map(lambda x: x - 5, [10, 20, 30, 40]))
list(map(lambda x: x * 3, [1, 2, 3, 4, 5]))
list(map(lambda c: (c * 9/5) + 32, [0, 20, 30, 40]))
list(map(lambda x: x > 50, [10, 60, 45, 80, 25]))

list(filter(lambda x:x%2==0,[1,2,3,4,5,6]))
list(filter(lambda x:x>10,[5,12,18,7,3]))
list(filter(lambda s:len(s)>5,["apple","banana","cherry","dog"]))
list(filter(lambda s:s!="",["hello","","world","","python"]))
list(filter(lambda x:x>0,[-5,3,0,8,-2]))
list(filter(lambda name:name.startswith('A'),["Alice","Bob","Anna","Tom"]))
list(filter(lambda x:x%3==0,[1,3,6,7,9,10]))
list(filter(lambda word:'e'in word,["cat","elephant","dog","bee"]))
list(filter(lambda x:x is not None,[1,None,2,None,3]))
list(filter(lambda x:x<=50,[10,60,45,80,25]))

