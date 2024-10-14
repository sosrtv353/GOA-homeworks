from turtle import *
width(7)
color("yellow")
forward(200) #lets make a house 1. walls
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200) 
left(90)      #end of the walls


begin_fill()
forward(70)  #start of the door
left(90)
color("green")

forward(100)
right(90)

forward(60)
right(90)

forward(100)
end_fill()   #end of the door
     
penup()      #start of the roof
goto(200, 200)    
pendown()   

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill() #end of the roof



penup()  #doorknob
goto(125,60)
color("brown")
pendown()
forward(1) #doorknob 

color("blue")
penup()   # start of windows
begin_fill()
goto(20,120)
left(210)
pendown()
forward(60)
right(90)

forward(55)
right(90)

forward(60)
right(90)
forward(55)
end_fill() #end of the left window

penup()  #start of right window
begin_fill()
goto(180,120)
pendown()
forward(55)
right(90)

forward(60)
right(90)

forward(55)
right(90) 

forward(60)
end_fill()


exitonclick()