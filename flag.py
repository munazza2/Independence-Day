# Republic day Animation

import turtle
import winsound
import os

# creating background screen
win = turtle.Screen()
win.setup(width=800,height=800)
win.bgpic("indian-flag-independence-day-india-august-15th-tricolor-red-3840x2160-2224.png")

# playing music
winsound.PlaySound('watan.wav',winsound.SND_ASYNC)





# Basement
flag = turtle.Turtle()
flag.speed(2)
flag.color("Black")
flag.pensize(5) 
flag.penup()
flag.goto(-450, -330)
flag.pendown()
flag.fillcolor("Brown")
flag.begin_fill()
for i in range(4):
    flag.left(90)
    flag.fd(30)
    flag.right(90)
    flag.fd(60)
    flag.right(90)
    flag.fd(30)
    flag.right(90)
    flag.fd(60)
    flag.right(180)
    flag.fd(60)
flag.end_fill()
flag.right(180)
flag.fd(240)
flag.right(90)
flag.fd(30)
flag.right(90)
flag.fd(30)
flag.left(90)
flag.begin_fill()
for j in range(3):
    flag.fd(30)
    flag.right(90)
    flag.fd(60)
    flag.right(90)
    flag.fd(30)
    flag.right(180)
flag.end_fill()
flag.left(90)
flag.fd(180)
flag.right(90)
flag.fd(30)
flag.right(90)
flag.fd(85)
flag.left(90)
flag.color("Black")
flag.begin_fill()


# Long stick
flag.fd(550)
flag.right(90)
flag.fd(5)
flag.right(90)
flag.fd(550)
flag.end_fill()
flag.right(180)
flag.fd(550)

# Flag
flag.speed(0)
flag.fillcolor("Orange")
flag.pensize(3)
flag.begin_fill()
flag.right(45)

flag.fillcolor("orange")

# Line 1
flag.begin_fill()
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.right(135)
flag.fd(45)
flag.left(135)
flag.right(180)

# Line 1 Reverse
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.end_fill()
flag.left(45)
flag.fd(45)
flag.right(180)
flag.right(45)

# Line 2

flag.fillcolor("Green")

flag.begin_fill()
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.right(135)
flag.fd(45)
flag.left(135)
flag.right(180)

# Line 2 Reverse
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.end_fill()
flag.left(45)
flag.right(180)
flag.fd(45)
flag.penup()
flag.right(45)
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(8):
    flag.fd(1.5)
    flag.left(1)
flag.pendown()

# Circle
flag.setheading(0)
flag.left(45)
flag.fd(5)
flag.setheading(0)
flag.pensize(3)
flag.color("Blue")
flag.circle(15)

flag.penup()
flag.left(90)
flag.fd(15)
flag.right(90)
flag.pendown()

# Ashoka Chakra
flag.pensize(1)
for i in range(24):
    flag.forward(15)
    flag.bk(15)
    flag.left(15)
flag.hideturtle()


# Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(1)
pen.color("Red")
pen.pensize(10)
pen.penup()
pen.goto(140, 0)
pen.pendown()


# writing text
text = turtle.Turtle()
text.hideturtle()
text.speed(2)

def write(message,pos,color):
    x,y = pos
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style = ('Courier',40,'italic')
    text.write(message,font=style)

write('Happy',(60,-100),'orange')
write('Indep',(0.1,-170),'white')
write('end',(158,-170),'blue')
write('ence',(250,-170),'white')
write('Day',(70,-220),'green')

turtle.done()