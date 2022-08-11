#HW13-LAB9-3-20191555-한영욱
import turtle
win=turtle.Screen()
t1=turtle.Turtle()
distance=15
trap=[89,-200,158,-248]
def getMinValue(v1,v2):
    if v1<v2:
        return v1
    return v2
def getMaxValue(v1,v2):
    if v1>v2:
        return v1
    return v2
def moveto(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
def isinTrap(x,y,trap):
    minX=getMinValue(trap[0],trap[2])
    maxX=getMaxValue(trap[0],trap[2])
    minY=getMinValue(trap[1],trap[3])
    maxY=getMaxValue(trap[1],trap[3])
    if x>=minX and x<=maxX and y>=minY and y<=maxY:
        return True
    return False
def showTrapRed(trap):
    t1.fillcolor('red')
    t1.begin_fill()
    moveto(trap[0],trap[1])
    t1.goto(trap[2],trap[1])
    t1.goto(trap[2],trap[3])
    t1.goto(trap[0],trap[3])
    t1.goto(trap[0],trap[1])
    t1.end_fill()
    moveto(trap[2]+distance,trap[3]+distance)
def keywest():
    position=t1.pos()
    t1.goto(position[0]-distance,position[1])
    if isinTrap(position[0]-distance,position[1],trap):
        showTrapRed(trap)
def keysouth():
    position=t1.pos()
    t1.goto(position[0],position[1]-distance)
    if isinTrap(position[0],position[1]-distance,trap):
        showTrapRed(trap)
def keynorth():
    position=t1.pos()
    t1.goto(position[0],position[1]+distance)
    if isinTrap(position[0],position[1]+distance,trap):
        showTrapRed(trap)
def keyeast():
    position=t1.pos()
    t1.goto(position[0]+distance,position[1])
    if isinTrap(position[0]+distance,position[1],trap):
        showTrapRed(trap)

            
def keyend():
    t1.penup()
    t1.home()
    t1.write('End')



win.setup(560,550)
win.bgpic('maze.gif')
t1.shape('turtle')
t1.color('blue')
t1.penup()
t1.goto(-100,-260)
t1.pendown()
win.onkey(keyeast,'Right')
win.onkey(keywest,'Left')
win.onkey(keysouth,'Down')
win.onkey(keynorth,'Up')
win.onkey(keyend,'e')
win.onkey(keyeast,'E')
win.listen()
turtle.mainloop()
