import turtle
#Create the screen instance
s = turtle.getscreen()
#Create Turtle instance
t = turtle.Turtle()
t.speed(15)
s.bgcolor("black")
cycle=1
while cycle<=72:
    if cycle%5==0:
        t.pencolor("purple")
    elif cycle%5==1:
        t.pencolor("blue")
    elif cycle%5==2:
        t.pencolor("green")
    elif cycle%5==3:
        t.pencolor("yellow")
    else:
        t.pencolor("red")
    t.circle(150)
    t.right(5)
    cycle+=1
turtle.done()
