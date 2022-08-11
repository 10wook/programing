#HW13-LAB9-1-20191555-한영욱
import turtle 
win=turtle.Screen()
t1=turtle.Turtle()
def moveto(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
def drawrectangle(x,y,wid,hi):
    moveto(x,y)
    t1.goto(x+wid,y)
    t1.goto(x+wid,y-hi)
    t1.goto(x,y-hi)
    t1.goto(x,y)
def drawtriagle(x,y,s):
    t1.setheading(0)
    moveto(x,y)
    t1.right(60)
    t1.forward(s)
    t1.right(120)
    t1.forward(s)
    t1.right(120)
    t1.forward(s)
w=turtle.window_width()
h=turtle.window_height()
dividedwidth=w/2
left=-(w/2)
right=w/2
left1=left
right1=left+dividedwidth
left2=right1
right2=right
shapewidth=dividedwidth*0.8
x1=left+dividedwidth*0.1
y1=h*0.1
x2=left2+dividedwidth*0.5
y2=h*0.1

drawrectangle(x1,y1,shapewidth,shapewidth)
t1.setheading(0)
drawtriagle(x2,y2,shapewidth)
