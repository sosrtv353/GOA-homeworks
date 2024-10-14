from turtle import *
color("gray")
begin_fill()
forward(250)
right(90)
forward(250)

right(90)
forward(600)
right(90) 

forward(250) 
right(90)
forward(350)

end_fill() #first progress

penup()
forward(25)
pendown()

begin_fill()
left(90)
forward(250)
left(90)
forward(180)

left(90)
forward(250)
end_fill()

color("red")
penup()
left(180)
forward(250)
pendown()
begin_fill()
right(45)
forward(125)
right(90)
forward(125)
end_fill()   
color("blue")
right(45)

penup()

forward(110)
right(90)
forward(44)
pendown()
begin_fill()
forward(90)
right(90)

forward(88)
right(90)

forward(90)
right(90)
forward(88)
end_fill()  #end of middle tower

color("gray")

penup()
left(90)
forward(270)
right(90)
pendown()
begin_fill()
forward(140)

right(90)
forward(130)
right(90)

forward(195)
right(90)
forward(130)
right(90)
forward(55)
end_fill() #right tower 1/2 done

begin_fill()
left(180)

forward(60)
forward(45)

left(90)
forward(45)

left(90)
forward(35)

right(90)
forward(30)

right(90)
forward(35)

left(90)
forward(55)

left(90)
forward(50) 
end_fill()   #end of right tower 2/2




color("yellow")
penup()
pendown()
begin_fill()
left(90)
forward(135)


right(140)
forward(85)

right(75)
forward(87)
end_fill()  #right tower flag

color("gray")
penup()

left(390)
forward(450)
left(90)
forward(230)

left(185)
pendown()
begin_fill()
forward(190)

right(90)
forward(110)
right(90)

forward(190)
end_fill() #left tower 1/2
begin_fill()
left(180)
forward(250)

left(90)
forward(45)

left(90)
forward(45)
right(90)
forward(35)
right(90)
forward(45)

left(90)
forward(35)
left(90)
forward(55)
end_fill() #end of left tower 2/2

color("yellow")
begin_fill()
left(410)
forward(80)
left(90)
forward(80)

left(130)
forward(120)
end_fill()
                #end of left tower flag

penup()
goto(21,-45)
right(270)
forward(39)
pendown()
color("brown")
begin_fill()
forward(160)
right(90)
forward(170)

right(90)
forward(160)


forward(16)
right(10)
forward(16)
right(12)
forward(16)
right(10)
forward(16)
right(12)
forward(16)
right(10)
forward(16)
right(12)
forward(16)
right(10)
forward(16)
right(12)
forward(16)
right(10)
forward(16)
right(12)
forward(17)
right(10)
forward(17)
right(12)
forward(17)
right(12)
forward(17)
right(12)
forward(17)
right(12)
forward(17)
right(12)
forward(17)
forward(10)
end_fill()   #castle doors




exitonclick()
