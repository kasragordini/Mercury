import math
import turtle
from turtle import left
a,b= input().split() #input a & b
a=int(a)
b=int(b)
wn = turtle.Screen()    # for build a turtle window
line = turtle.Turtle()  # for build a turtle line
line.hideturtle()
line.color("black")
line.pensize(2)
line.speed(5)
for i in range(2): # for the rectangular
    line.fd(b)  #one of the rectangular side size is b
    line.left(90)   
    line.fd(a)  #one of the rectangular side size is a
    line.left(90)
d = (math.atan(a/b))* 180/math.pi   #size of angel
line.left(d)
c = math.sqrt(((a)**2)+((b)**2))    #size of diameter #sqrt=radikal
line.fd(c)  #fd=forward bk=backward left=lt right=rt 
line.home()
line.fd(b)
line.left(90 + (90-d))
line.fd(c)