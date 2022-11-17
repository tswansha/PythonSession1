import turtle
#Create the screen instance
s = turtle.getscreen()
#Create Turtle instance
t = turtle.Turtle()
t.speed(15)
s.bgcolor("black")
count=100
while count>=-100:
    if count%5==0:
        t.pencolor("red")
    elif count%5==1:
        t.pencolor("orange")
    elif count%5==2:
        t.pencolor("yellow")
    elif count%5==3:
        t.pencolor("lightgreen")
    elif count%5==4:
        t.pencolor("magenta")
    else:
        t.pencolor("white")
    t.circle(count)
    count-=3
turtle.done()
