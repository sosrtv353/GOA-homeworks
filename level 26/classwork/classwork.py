def greeting(name):
     print("hello name")
greeting()
#classwork 1 done

def manual_range(start, end, step):
    range1 = range(start, end, step)

    for i in range1:
        if i %2 == 0: print(i)

manual_range(2, 20, 2)
manual_range(20, 120, 5)
manual_range(1, 21, 6)
manual_range(24, 270, 21)
manual_range(20, 200, 10)

#classwork 2 done

def manual_len(li):
     count=0
     for i in li:
          count+=1
     print(count)
manual_len([4,6,7,8])
#classwork 3 done