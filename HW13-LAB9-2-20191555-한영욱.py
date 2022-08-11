#HW13-LAB9-2-20191555-한영욱
import turtle
import random
linet=turtle.Turtle()
linet.penup()
linet.setposition(200,50)
linet.pendown()
linet.setposition(200,-50)

linet.hideturtle()
T=turtle.Turtle()
T.shape('turtle')
T.penup()
T.setposition(-100,20)

S=turtle.Turtle()
S.shape('turtle')
S.penup()
S.setposition(-100,-20)
ss=0
ts=0
while ((ts<300) and (ss<300)):
    td=random.randint(1,10)
    T.forward(td)
    ts+=td

    sd=random.randint(1,10)
    S.forward(sd)
    ss+=sd
if ts>sd:
    T.color('blue')
    S.color('red')
else:
    T.colcor('red')
    S.color('blue')
