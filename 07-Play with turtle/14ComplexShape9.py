import turtle
#Create the screen instance
s = turtle.getscreen()
#Create Turtle instance
t = turtle.Turtle()
t.speed(15)
s.bgcolor("black")
#Increase the speed of Turtle
turtle.speed(20)
cycle=1
while cycle<=72:
    if cycle%5==0:
        t.pencolor("red")
    elif cycle%5==1:
        t.pencolor("orange")
    elif cycle%5==2:
        t.pencolor("yellow")
    elif cycle%5==3:
        t.pencolor("lightgreen")
    elif cycle%5==4:
        t.pencolor("magenta")
    else:
        t.pencolor("white")
    count=1
    while count<=4:
        t.forward(300)
        t.right(120)
        count+=1
    cycle+=1
    t.right(5)
#Wait untill close the screen
turtle.done()
