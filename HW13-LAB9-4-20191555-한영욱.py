#HW13-LAB9-4-20191555-한영욱
import turtle
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
def drawstar(x,y,s):
    t1.setheading(0)
    moveto(x,y)
    t1.forward(s)
    t1.right(144)
    t1.forward(s)
    t1.right(144)
    t1.forward(s)
    t1.right(144)
    t1.forward(s)
    t1.right(144)
    t1.forward(s)
    t1.right(144)
    
w=turtle.window_width()
h=turtle.window_height()
dividedwidth2=w/2
dividedwidth3=w/3
left=-(w/2)
right=w/2
left1=left
right1=left+dividedwidth3
left2=right1
right2=left2+dividedwidth3
left3=right2
right3=right
shapewidth=dividedwidth3*0.8
x1=left+dividedwidth3*0.1
y1=h*0.1
x2=left2+dividedwidth3*0.5
y2=h*0.1
x3=left3+dividedwidth3*0.1
y3=0

drawrectangle(x1,y1,shapewidth,shapewidth)
t1.setheading(0)
drawtriagle(x2,y2,shapewidth)
t1.setheading(0)
drawstar(x3,y3,shapewidth)
